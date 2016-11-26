from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render, render_to_response

from core.forms import NewUserForm
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
                    # stylist.stylist_picture
                    stylist.save()

                    user = User.objects.get(username=create_user_form.data['username'])
                    user.stylist = stylist
                    user.save()

                    return render(request, 'core/newUserLogin.html')

                else:
                    customer = Customer()
                    # customer.customer_picture
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
                return render(request, 'core/loggedin.html', {'full_name': request.user.get_full_name()})
            else:
                return render(request, 'core/invalidLogin.html')