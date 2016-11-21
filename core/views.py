from django.http import HttpResponse
from django.shortcuts import render, render_to_response

from core.forms import NewUserForm
from customer.models import Customer
from stylist.models import Stylist, User


def index(request):
    return render(request, 'core/home.html')

def entering_user(request):
    if request.method == 'POST':

        if request.POST.get('Submit') == 'CREATE':
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