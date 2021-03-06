"""
    Customer Views.
"""
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from core.utils.view_logic import UserLogic, CookieClearer
from customer.forms import NewAppointmentForm, StylistApplicationForm
from core.models import User, Appointment, ItemInBill, Review
from datetime import datetime

# for the search
from functools import reduce
from operator import __or__ as OR

# from django.db.models import Q,
from customer.utils.view_logic import CustomerLogic
from stylist.models import PortfolioHaircut, StylistMenu
from stylist.utils.view_logic import BillLogic

'''
    NAV BAR OPTION
'''


def profile(request):
    if request.user.is_stylist == 'NO':
        return render(request, 'customer/customerReal/profile/profile.html',
                      {'full_name': request.user.get_full_name(),
                       'customer': request.user})
    else:
        return redirect('core:logout')


def dashboard(request):
    return CustomerLogic.render_dashboard(request)


def become_stylist(request):
    """
        View that handles a user's application to be a stylist.
    """
    if request.method == 'POST':
        stylist_application = StylistApplicationForm(request.POST)

        if stylist_application.is_valid():
            stylist_application = stylist_application.save(commit=False)
            stylist_application.applicant = request.user
            stylist_application.save()
            return render(request, 'customer/stylistApplications/application_submitted.html')

        else:
            return render(request, 'customer/stylistApplications/application_error.html')

    elif request.method == 'GET':
        return CustomerLogic.render_application_status(request)

    else:
        return redirect('core:logout')


'''
    APPOINTMENTS
'''


def appointments(request):
    """
        Provides all appointments that the user is involved in.
    """
    if CustomerLogic.is_customer(request):
        pending_appointments = Appointment.objects.filter(customer=request.user,
                                                          status=Appointment.STATUS_PENDING)
        accepted_appointments = Appointment.objects.filter(customer=request.user,
                                                           status=Appointment.STATUS_ACCEPTED)
        declined_appointments = Appointment.objects.filter(customer=request.user,
                                                           status=Appointment.STATUS_DECLINED)

        rescheduled_appointments = Appointment.objects.filter(
            (Q(status=Appointment.STATUS_RESCHEDULED_BYCUSTOMER) | Q(status=Appointment.STATUS_RECHEDULED_BYSTYLIST)),
            customer=request.user)
        completed_appointments = Appointment.objects.filter(customer=request.user,
                                                            status=Appointment.STATUS_COMPLETED)

        return render(request, 'customer/customerReal/dashboard/appointments/customer_appointment.html',
                      {'full_name': request.user.get_full_name(),
                       'stylist_reschedule': Appointment.STATUS_RECHEDULED_BYSTYLIST,
                       'customer_reschedule': Appointment.STATUS_RESCHEDULED_BYCUSTOMER,
                       'pending_appointments': pending_appointments,
                       'accepted_appointments': accepted_appointments,
                       'declined_appointments': declined_appointments,
                       'rescheduled_appointments': rescheduled_appointments,
                       'completed_appointments': completed_appointments})
    else:
        return redirect('core:logout')


'''
    CREATE APPOINTMENT VIEWS
'''


def create_appointment(request):
    """
        Probably the most complicated method in this app.
        | A lot of information is required before a POST can be succesfully sent to this view.
        |
        | Information necessary for this method:
            :param stylist_pk: pk value of the stylist
            :param portfolio_haircut: pk value of the selected haircut (optional)
            :param stylist_menu_pk: pk value of an option in the stylist's menu (optional)
            :param date: Appointment date
        | Either the portfolio_haircut or the stylist_menu_pk should be included
        | Once the appointment is created the price of the appointment is updated.
        | The cookies are then finally cleared.
    """
    if request.method == 'POST':
        create_appointment_form = NewAppointmentForm(request.POST)

        if create_appointment_form.is_valid():

            new_appointment = create_appointment_form.save(commit=False)
            new_appointment.customer = request.user
            new_appointment.stylist = User.objects.get(pk=request.session['stylist_pk'])
            new_appointment.start_date_time = request.session['calendar_event'].get('start')
            new_appointment.end_date_time = request.session['calendar_event'].get('end')
            new_appointment.title = request.session['calendar_event'].get('title')
            new_appointment.save()

            if 'portfolio_haircut' in request.session:
                portfolio_haircut = PortfolioHaircut.objects.get(pk=request.session['portfolio_haircut'])
                ItemInBill.objects.create(item_portfolio=portfolio_haircut, price=portfolio_haircut.price,
                                          appointment=new_appointment)

            if 'stylist_menu_pk' in request.session:
                stylist_option = StylistMenu.objects.get(pk=request.session['stylist_menu_pk'])
                ItemInBill.objects.create(item_menu=stylist_option, price=stylist_option.price,
                                          appointment=new_appointment)

            BillLogic.update_price(appointment=new_appointment)
            CookieClearer.appointment_cookies(request)
            return redirect('customer:dashboard')
        else:
            print(create_appointment_form.errors)
        return redirect('customer:dashboard')

    # ToDo: You can get rid of the following if/else statement and just use template code: {{ chosen_stylist.username | default_if_none:"PleaseSelectStylsit" }}
    # if 'stylist_pk' in request.session:
    #     chosen_stylist = User.objects.get(pk=request.session['stylist_pk'])
    # else:
    #     chosen_stylist = 'Please select a stylist'
    else:
        stylist_list = User.objects.filter(is_stylist='YES')

    return render(request, 'customer/customerReal/search/search_core.html',
                  {'stylist_list': stylist_list})


'''
    CREATE APPOINTMENT HELPERS
'''


# Todo: add more functionality
def stylist_search(request):
    """
        METHODS ALLOWED = [GET]
            :param param: search parameter

        The very first step in creating an appointment is finding a stylist. This view renders a list of stylists that
        match the search parameter.
    """
    if 'param' in request.GET:
        stylist_list = User.objects.filter(is_stylist='YES', first_name__icontains=request.GET.get('param'))
    else:
        stylist_list = None
    return render(request, 'customer/stylist_search.html', {
        'stylist_list': stylist_list
    })


def obtain_stylist_profile(request):
    """
        METHODS ALLOWED = [GET]
            :param stylist_pk: pk value of stylist

        The second step in creating an appointment.
        | After the customer clicks on a stylist from the stylist search page they need to view the stylist's profile.
        | This view renders the stylist's portfolio.
        | From the stylist's portfolio the customer can then select a haircut or menu option.
    """
    if request.user.is_authenticated:
        if request.method == 'GET':
            if 'stylist_pk' in request.GET:
                stylist = User.objects.get(pk=request.GET.get('stylist_pk'), is_stylist='YES')
                portfolio_haircuts = PortfolioHaircut.objects.filter(stylist=stylist)
                stylist_options = StylistMenu.objects.filter(stylist=stylist)
                return render(request, 'customer/stylist_profile.html',
                              {'stylist': stylist, 'portfolio_haircuts': portfolio_haircuts,
                               'stylist_options': stylist_options})
        return redirect('customer:create_appointment')
    else:
        return redirect('core:logout')


def obtain_selected_haircut(request):
    """
        METHODS ALLOWED = [POST]

        The pk value of the selected haircut and the stylist are stored in Django sessions.
        | The user is redirected to the create appointment view to set a date for the appointment.
    """
    if request.user.is_authenticated:
        if request.method == 'POST':
            request.session['portfolio_haircut'] = request.POST.get('portfolio_haircut')
            request.session['stylist_pk'] = request.POST.get('stylist_pk')
        return redirect('customer:schedule_appointment')
    else:
        return redirect('core:logout')


def obtain_selected_menuOption(request):
    """
        METHODS ALLOWED = [POST]

        The pk value of the selected menu option and the stylist are stored in Django sessions.
        | The user is redirected to the create appointment view to set a date for the appointment.
    """
    if request.user.is_authenticated:
        if request.method == 'POST':
            request.session['stylist_menu_pk'] = request.POST.get('stylist_option_pk')
            request.session['stylist_pk'] = request.POST.get('stylist_pk')
        return redirect('customer:schedule_appointment')
    else:
        return redirect('core:logout')


def schedule_appointment(request):
    if request.method == 'GET':
        if 'stylist_menu_pk' in request.session:
            menu_object = StylistMenu.objects.get(pk=request.session['stylist_menu_pk'])
            duration = menu_object.duration
            title = menu_object.name
        elif 'portfolio_haircut' in request.session:
            portfolio_haircut = PortfolioHaircut.objects.get(pk=request.session['portfolio_haircut'])
            duration = portfolio_haircut.duration
            title = portfolio_haircut.name
        else:
            duration = 0
            title = ''
        return render(request, 'customer/calendar/stylist_shift.html', {'stylist_pk': request.session['stylist_pk'],
                                                                        'duration': duration,
                                                                        'title': title})
    if request.method == 'POST':
        calendar_event = {
            'start': request.POST.get('start'),
            'end': request.POST.get('end'),
            'title': request.POST.get('title')
        }
        request.session['calendar_event'] = calendar_event
        return JsonResponse(data={'url': reverse('customer:create_appointment')})


'''
    APPOINTMENT MODIFIERS
'''


# todo: can this be utilized by both stylist's and customers?
def accept_appointment(request):
    """
        METHODS ALLOWED = [POST]
            :param appointment_pk: pk value of the appointment

        Only available to customers. When a stylist makes a schedule change the customer needs to 'accept' it.
    """
    if CustomerLogic.is_customer(request):
        if request.method == 'POST':
            appointment = Appointment.objects.get(pk=request.POST.get('appointment_pk'))
            appointment.status = Appointment.STATUS_ACCEPTED
            appointment.save()
            return redirect('customer:dashboard')
    else:
        return redirect('core:logout')


def cancel_appointment(request):
    """
        METHODS ALLOWED = [POST]
            :param appointment_pk: pk value of the appointment

        Customers can cancel or decline an appointment by sending a POST request to this view.
    """
    if CustomerLogic.is_customer(request):
        if request.method == 'POST':
            appointment = Appointment.objects.get(pk=request.POST.get('appointment_pk'))
            appointment.status = Appointment.STATUS_DECLINED
            appointment.save()
            return redirect('customer:dashboard')
    else:
        return redirect('core:logout')


def reschedule_appointment(request):
    """
        METHODS ALLOWED = [POST]
            :param appointment_pk: pk value of the appointment
            :param date: new appointment date

        Customers intending on rescheduling the appointment must send a POST request to this view.
    """
    if request.user.is_stylist == 'NO':
        if request.method == 'POST':
            appointment = Appointment.objects.get(pk=request.POST.get('appointment_pk'))
            appointment.status = Appointment.STATUS_RESCHEDULED_BYCUSTOMER
            appointment.date = datetime.strptime(request.POST.get('date'), '%Y-%m-%dT%H:%M')
            appointment.save()
            return redirect('customer:dashboard')
    else:
        return redirect('core:logout')


'''
     Bill
'''


# todo: should customers be able to modify the bill (add or remove items) before the appointment is accepted?
# todo: why is the appointment_pk value stored in sessions here?
def view_bill(request):
    """
        METHODS ALLOWED = [GET]
            :param appointment_pk: pk value of the appointment.

        All ItemInBill entries are retrieved for the particular appointment and the appointment_pk value is saved.
    """
    if CustomerLogic.is_customer(request):
        if request.method == 'GET':
            appointment = Appointment.objects.get(pk=request.GET.get('appointment_pk'))
            bill = ItemInBill.objects.filter(appointment=appointment)
            request.session['appointment_for_bill'] = request.GET.get('appointment_pk')
            return render(request, 'customer/view_bill.html', {'bill': bill})
        else:
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('core:logout')


'''
    REVIEW
'''


def submit_review(request):
    """
        METHODS ALLOWED = [POST]
            :param review_pk: pk value of the review

        The stylist_rating on the review object is updated through this review. Once the stylist_rating is updated
        all the averages are recalculated through UserLogic.update_average(review).
    """
    if CustomerLogic.is_customer(request):
        if request.method == 'POST':
            review = Review.objects.get(pk=request.POST.get('review_pk'))
            review.stylist_rating = int(request.POST.get('rating'))
            review.save()
            UserLogic.update_average(review)
            return redirect('customer:dashboard')
    else:
        return redirect('core:logout')


'''
    SEARCH FOR THESIS
'''


def search_core(request):
    """
        For thesis.
    """
    stylist_list = User.objects.filter(is_stylist='YES')
    CookieClearer.thesis_search(request)
    return render(request, 'customer/customerReal/search/search_for_thesis/base.html', {'stylist_list': stylist_list})


def render_stylist_data(request):
    """
        For Thesis
    """
    if request.method == 'GET':
        request.session['stylist_pk'] = request.GET.get('stylist_pk')
        stylist = User.objects.get(pk=request.GET.get('stylist_pk'))
        menu_list = StylistMenu.objects.filter(stylist=stylist)
        portfolio_list = PortfolioHaircut.objects.filter(stylist=stylist)
        stylist_list = User.objects.filter(is_stylist='YES')
        return render(request, 'customer/customerReal/search/search_for_thesis/base.html', {'stylist': stylist,
                                                                                            'menu_list': menu_list,
                                                                                            'portfolio_list': portfolio_list,
                                                                                            'stylist_list': stylist_list})
    else:
        redirect('core:logout')


def save_haircut(request):
    """
        For Thesis
    """
    if request.method == 'POST':
        request.session["haircut_pk"] = request.POST.get('haircut_pk')
        return redirect('customer:reveal_fullcalendar')
    else:
        return redirect('core:logout')


def save_menu(request):
    """
        For Thesis
    """
    if request.method == 'POST':
        request.session['menu_pk'] = request.POST.get('menu_pk')
        return redirect('customer:reveal_fullcalendar')


def reveal_fullcalendar(request):
    """
        For Thesis
    """
    if 'haircut_pk' in request.session:
        haircut = PortfolioHaircut.objects.get(pk=request.session.get('haircut_pk'))
        duration = haircut.duration
    elif 'menu_pk' in request.session:
        menu = StylistMenu.objects.get(pk=request.session.get('menu_pk'))
        duration = menu.duration
    else:
        duration = None

    return render(request, 'customer/customerReal/search/search_for_thesis/calendar.html',
                  {'stylist_pk': request.session.get('stylist_pk'),
                   'menu_pk': request.session.get('menu_pk'),
                   'haircut_pk': request.session.get('haircut_pk'),
                   'duration': duration})
