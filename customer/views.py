"""
    Customer Views.
"""
from django.shortcuts import render, redirect

from core.utils.view_logic import UserLogic, CookieClearer
from customer.forms import NewAppointmentForm, StylistApplicationForm
from core.models import User, Appointment, ItemInBill, Review, StylistMenu
from datetime import datetime

# for the search
from functools import reduce
from operator import __or__ as OR

# from django.db.models import Q,
from customer.utils.view_logic import CustomerLogic
from stylist.models import PortfolioHaircut
from stylist.utils.view_logic import BillLogic

'''
    NAV BAR OPTION
'''


def profile(request):
    if request.user.is_stylist == 'NO':
        return render(request, 'customer/profile.html',
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
            new_appointment.date = datetime.strptime(request.POST.get('date'), '%Y-%m-%dT%H:%M')
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
    if 'stylist_pk' in request.session:
        chosen_stylist = User.objects.get(pk=request.session['stylist_pk'])
    else:
        chosen_stylist = 'Please select a stylist'

    return render(request, 'customer/create_appointment.html',
                  {'chosen_stylist': chosen_stylist})


'''
    CREATE APPOINTMENT HELPERS
'''

#Todo: add more functionality
def stylist_search(request):
    """

    """
    if 'param' in request.GET:
        stylist_list = User.objects.filter(is_stylist='YES', first_name__icontains=request.GET.get('param'))
    else:
        stylist_list = None
    return render(request, 'customer/stylist_search.html', {
        'stylist_list': stylist_list
    })


def obtain_stylist_profile(request):
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
    if request.user.is_authenticated:
        if request.method == 'POST':
            request.session['portfolio_haircut'] = request.POST.get('portfolio_haircut')
            request.session['stylist_pk'] = request.POST.get('stylist_pk')
        return redirect('customer:create_appointment')
    else:
        return redirect('core:logout')


def obtain_selected_menuOption(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            request.session['stylist_menu_pk'] = request.POST.get('stylist_option_pk')
            request.session['stylist_pk'] = request.POST.get('stylist_pk')
        return redirect('customer:create_appointment')
    else:
        return redirect('core:logout')


#ToDo: Is this view even being used?
def catch_menu_choices(request):
    if request.method == 'POST':
        request.session['menu_main'] = request.POST.get('menu_main')
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect(request.META.get('HTTP_REFERER'))


'''
    APPOINTMENT MODIFIERS
'''


def accept_appointment(request):
    if request.user.is_stylist == 'NO':
        if request.method == 'POST':
            appointment = Appointment.objects.get(pk=request.POST.get('appointment_pk'))
            appointment.status = Appointment.STATUS_ACCEPTED
            appointment.save()
            return redirect('customer:dashboard')
    else:
        return redirect('core:logout')


def cancel_appointment(request):
    if request.user.is_stylist == 'NO':
        if request.method == 'POST':
            appointment = Appointment.objects.get(pk=request.POST.get('appointment_pk'))
            appointment.status = Appointment.STATUS_DECLINED
            appointment.save()
            return redirect('customer:dashboard')
    else:
        return redirect('core:logout')


def reschedule_appointment(request):
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
    APPOINTMENT MODIFIERS
'''


def view_bill(request):
    if request.user.is_stylist == 'NO':
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
    if request.user.is_stylist == 'NO':
        if request.method == 'POST':
            review = Review.objects.get(pk=request.POST.get('review_pk'))
            review.stylist_rating = int(request.POST.get('rating'))
            review.save()
            UserLogic.update_average(review)
            return redirect('customer:dashboard')
    else:
        return redirect('core:logout')


'''
    Adam Lynch's Portion.
'''


def dashboard_real(request):
    if request.user.is_stylist == 'NO':
        return render(request, 'customer/customerReal/dashboard/dashboard_core.html')
    else:
        return redirect('core:logout')


def profile_real(request):
    if request.user.is_stylist == 'NO':
        return render(request, 'customer/customerReal/profile/profile_core.html')
    else:
        return redirect('core:logout')


def search_real(request):
    if request.user.is_stylist == 'NO':
        return render(request, 'customer/customerReal/search/search_core.html')
    else:
        return redirect('core:logout')


def settings_real(request):
    if request.user.is_stylist == 'NO':
        return render(request, 'customer/customerReal/settings/settings_core.html')
    else:
        return redirect('core:logout')
