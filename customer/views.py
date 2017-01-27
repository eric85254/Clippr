from django.shortcuts import render, redirect

from customer.forms import NewAppointmentForm, StylistApplicationForm
from core.models import User, Appointment, Application, ItemInBill, Menu
from datetime import datetime

# for the search
from functools import reduce
from operator import __or__ as OR


# from django.db.models import Q,
from stylist.models import PortfolioHaircut


def profile(request):
    if request.user.is_stylist == 'NO':
        full_name = request.user.get_full_name()
        if request.user.profile_picture is not None:
            customer = request.user
        else:
            customer = None
        return render(request, 'customer/profile.html',
                      {'full_name': full_name,
                       'customer': customer})
    else:
        return redirect('core:logout')


def dashboard(request):
    if request.user.is_stylist == 'NO':
        if Appointment.objects.filter(customer=request.user).exists():
            appointment_list = Appointment.objects.filter(customer=request.user)

        else:
            appointment_list = None
        return render(request, 'customer/dashboard.html', {'full_name': request.user.get_full_name(),
                                                           'appointments': appointment_list})
    else:
        return redirect('core:logout')


def catch_menu_choices(request):
    if request.method == 'POST':
        request.session['menu_main'] = request.POST.get('menu_main')
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect(request.META.get('HTTP_REFERER'))


def stylist_search(request):
    if 'param' in request.GET:
        stylist_list = User.objects.filter(username__icontains=request.GET.get('param'), is_stylist='YES')
    else:
        stylist_list = None
    return render(request, 'customer/stylist_search.html', {
        'stylist_list': stylist_list
    })


def become_stylist(request):
    if request.user.is_stylist == 'NO':
        if request.method == 'POST':
            stylist_application = StylistApplicationForm(request.POST)

            if stylist_application.is_valid():
                stylist_application = stylist_application.save(commit=False)
                stylist_application.applicant = request.user
                stylist_application.save()
                return render(request, 'customer/stylistApplications/application_submitted.html')

            else:
                return render(request, 'customer/stylistApplications/application_error.html')

        application = Application.objects.filter(applicant=request.user)
        if len(application) > 0:
            application = Application.objects.get(applicant=request.user)
            if application.application_status == 'PENDING':
                return render(request, 'customer/stylistApplications/application_submitted.html')
            elif application.application_status == 'SCHEDULED':
                return render(request, 'customer/stylistApplications/interview_scheduled.html',
                              {'application': application})
            elif application.application_status == 'REJECTED':
                return render(request, 'customer/stylistApplications/application_rejected.html')
        else:
            return render(request, 'customer/stylistApplications/become_stylist.html')
    else:
        return redirect('core:logout')


def create_appointment(request):
    if request.method == 'POST':
        create_appointment_form = NewAppointmentForm(request.POST)

        if create_appointment_form.is_valid():
            new_appointment = create_appointment_form.save(commit=False)
            new_appointment.customer = request.user
            new_appointment.stylist = User.objects.get(username=request.session['username'])
            new_appointment.date = datetime.strptime(request.POST.get('date'), '%Y-%m-%dT%H:%M')
            new_appointment.save()

            menu_item = Menu.objects.get(name=request.session['menu_main'])
            bill = ItemInBill.objects.create(item_menu=menu_item, price=1.00, appointment=new_appointment)
            bill.save()

            return redirect('customer:dashboard')
        else:
            print(create_appointment_form.errors)
        return redirect('customer:dashboard')

    if 'username' in request.session:
        chosen_stylist = User.objects.get(username=request.session['username'])
    else:
        chosen_stylist = 'Please select a stylist'
    if 'menu_main' in request.session:
        menu_main = Menu.objects.filter(category__icontains='main').get(name__icontains=request.session['menu_main'])
    else:
        menu_main = None

    return render(request, 'customer/create_appointment.html',
                  {'chosen_stylist': chosen_stylist, 'menu_main': menu_main})


def create_appointment_obtainStylistUsername(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            request.session['username'] = request.POST.get('username')
        return redirect('customer:create_appointment')
    else:
        return redirect('core:logout')


def create_appointment_menuMainChoice(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            request.session['menu_main'] = request.POST.get('menu_main')
        return redirect('customer:create_appointment')
    else:
        return redirect('core:logout')


def obtain_stylist_profile(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            if 'username' in request.GET:
                stylist = User.objects.get(username__icontains=request.GET.get('username'), is_stylist='YES')
                portfolio_haircuts = PortfolioHaircut.objects.filter(stylist=stylist)
                return render(request, 'customer/stylist_profile.html', {'stylist': stylist, 'portfolio_haircuts': portfolio_haircuts})
        return redirect('customer:create_appointment')
    else:
        return redirect('core:logout')