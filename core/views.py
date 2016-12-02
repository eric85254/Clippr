from django.contrib import auth
from django.shortcuts import render, redirect

from core.forms import NewUserForm
from core.utils.global_constants import DEFAULT_PICTURE_LOCATION
from customer.models import Customer
from stylist.models import Stylist, User


def index(request):
    return render(request, 'core/home.html', {'form': None})


def returning_user(request):
    return render(request, 'core/login.html', {'form': None})


def entering_user(request):
    if request.method == 'POST':

        if 'CREATE' in request.POST:
            create_user_form = NewUserForm(request.POST)

            if create_user_form.is_valid():
                create_user_form.save()

                if create_user_form.data['is_stylist'] == 'YES':
                    stylist = Stylist()
                    stylist.stylist_picture = DEFAULT_PICTURE_LOCATION
                    stylist.save()

                    user = User.objects.get(username=create_user_form.data['username'])
                    user.stylist = stylist
                    user.save()

                    return render(request, 'core/newUserLogin.html')

                else:
                    customer = Customer()
                    customer.customer_picture = DEFAULT_PICTURE_LOCATION
                    customer.save()

                    user = User.objects.get(username=create_user_form.data['username'])
                    user.customer = customer
                    user.save()

                    return render(request, 'core/newUserLogin.html')

            else:
                print(create_user_form.errors)
                return render(request, 'core/home.html', {'form': create_user_form})

        elif 'LOGIN' in request.POST:
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                if user.is_stylist == 'YES':
                    return redirect('stylist:profile')
                else:
                    return redirect('customer:profile')
            else:
                return render(request, 'core/invalidLogin.html')


def upload_picture(request):
    if request.method == 'POST':
        if 'PICTURE' in request.POST:
            if request.user.is_stylist == 'YES':
                stylist = request.user.stylist
                stylist.stylist_picture = request.FILES['profile_picture']
                stylist.save()
                return redirect('stylist:profile')
            else:
                customer = request.user.customer
                customer.customer_picture = request.FILES['profile_picture']
                customer.save()
                return redirect('customer:profile')
        else:
            return redirect('core:upload_picture')
    else:
        return render(request, 'core/upload_picture.html')


def logout(request):
    auth.logout(request)
    return redirect('core:home')


def home(request):
    return render(request, 'core/Home.html')


def basic_information(request):
    if request.method == 'POST':
        if 'BASIC' in request.POST:
            if request.user.is_stylist == 'YES':
                stylist = request.user.stylist
                stylist.location = request.POST.get('location')
                stylist.biography = request.POST.get('basic_information')
                stylist.save()
                return redirect('stylist:profile')
            else:
                customer = request.user.customer
                customer.location = request.POST.get('location')
                customer.biography = request.POST.get('basic_information')
                customer.save()
                return redirect('customer:profile')
    else:
        if request.user.is_stylist == 'YES':
            stylist = request.user.stylist
            return render(request, 'core/basic_information.html', {'user': stylist})
        else:
            customer = request.user.stylist
            return render(request, 'core/basic_information.html', {'user': customer})
