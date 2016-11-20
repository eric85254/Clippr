from django.http import HttpResponse
from django.shortcuts import render, render_to_response

from core.forms import NewUserForm
from stylist.models import Stylist


def index(request):
    return render(request, 'core/home.html')

def create_new_user(request):
    if request.method == 'POST':
        if request.POST.get('Submit') == 'CREATE':
            create_user_form = NewUserForm(request.POST)
            if create_user_form.is_stylist == 'YES':
                if create_user_form.is_valid():
                    stylist = Stylist()
                    stylist.name = "test"
                    stylist.email = "test@gmail.com"
                    # stylist.stylist_picture
                    stylist.save()

                    create_user_form.stylist = stylist
                    create_user_form.save()


                    return render(request, 'core/newUserLogin.html')