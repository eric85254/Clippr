from django.shortcuts import render, redirect

from customer.forms import NewAppointmentForm
from stylist.models import Appointments
from core.models import User

# for the search
from functools import reduce
from operator import __or__ as OR
from django.db.models import Q


def profile(request):
    full_name = request.user.get_full_name()
    if request.user.profile_picture is not None:
        customer = request.user
    else:
        customer = None
    return render(request, 'customer/profile.html',
                  {'full_name': full_name,
                   'customer': customer})


def dashboard(request):
    if Appointments.objects.filter(customer=request.user).exists():
        appointment_list = Appointments.objects.filter(customer=request.user)

    else:
        appointment_list = None
    return render(request, 'customer/dashboard.html', {'full_name': request.user.get_full_name(),
                                                       'appointments': appointment_list})


def create_appointment(request):
    if request.method == 'POST':
        if 'SELECT' in request.POST:
            request.session['username'] = request.POST.get('username')
            return redirect('customer:create_appointment')

        if 'CREATE' in request.POST:
            create_appointment_form = NewAppointmentForm(request.POST)

            if create_appointment_form.is_valid():
                new_appointment = create_appointment_form.save(commit=False)
                new_appointment.customer = request.user
                new_appointment.stylist = User.objects.get(username=request.session['username'])
                new_appointment.location = request.POST.get('location')
                # new_appointment.date = datetime.now
                new_appointment.save()

                return redirect('customer:dashboard')
            else:
                print(create_appointment_form.errors)
        return redirect('customer:dashboard')
    else:
        if 'username' in request.session:
            chosen_stylist = User.objects.get(username=request.session['username'])
        else:
            chosen_stylist = 'Please select a stylist'
        return render(request, 'customer/create_appointment.html', {'chosen_stylist': chosen_stylist})


def stylist_search(request):
    if 'param' in request.GET:
        stylist_list = User.objects.filter(username__icontains=request.GET.get('param'), is_stylist='YES')
    else:
        stylist_list = None
    return render(request, 'customer/stylist_search.html', {
        'stylist_list': stylist_list
    })