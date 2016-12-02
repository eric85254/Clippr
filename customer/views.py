from django.shortcuts import render, redirect

from customer.forms import NewAppointmentForm
from stylist.models import User

# for the search
from functools import reduce
from operator import __or__ as OR
from django.db.models import Q


def profile(request):
    full_name = request.user.get_full_name()
    if request.user.customer.customer_picture is not None:
        customer = request.user.customer
    else:
        customer = None
    return render(request, 'customer/profile.html',
                  {'full_name': full_name,
                   'customer': customer})


def dashboard(request):
    return render(request, 'customer/dashboard.html', {'full_name': request.user.get_full_name()})


def create_appointment(request, username):
    if request.method == 'GET':
        if 'SEARCH' in request.GET:
            redirect('customer:stylist_search', param=request.GET.get('stylist_search'))
    if request.method == 'POST':
        create_appointment_form = NewAppointmentForm(request.POST)
        create_appointment_form.customer = request.user.customer
        return None
    else:
        if username is not None:
            chosen_stylist = username
        else:
            chosen_stylist = 'Please select a stylist'
        return render(request, 'customer/create_appointment.html', {'chosen_stylist': chosen_stylist})


def stylist_search(request, param):
    search_result_list = User.objects.filter(username__icontains=param)
