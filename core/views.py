from django.contrib import auth
from django.http import JsonResponse
from django.shortcuts import render, redirect

from core.forms import NewUserForm, UserInformation
from core.utils.global_constants import DEFAULT_PICTURE_LOCATION
from core.utils.view_logic import UserLogic

'''
    Create User
        Didn't migrate code to view_logic.py because it involves JsonResponse stuff
'''


def create_user(request):
    if request.method == 'POST':
        create_user_form = NewUserForm(request.POST)

        if create_user_form.is_valid():
            new_user = create_user_form.save(commit=False)
            new_user.profile_picture = DEFAULT_PICTURE_LOCATION
            new_user.save()
            data = {
                'success': True
            }
            return JsonResponse(data=data)
            # return redirect(request.META.get('HTTP_REFERER'))

        else:
            print(create_user_form.errors)
            data = create_user_form.errors
            data['success'] = False
            return JsonResponse(data=data)
            # return redirect(request.META.get('HTTP_REFERER'))


'''
    Returning User
'''


def returning_user(request):
    if request.method == 'GET':
        return redirect('core:home')

    if request.method == 'POST':
        user = UserLogic.retrieve_user(request)
        UserLogic.login(request, user)
        return UserLogic.redirect_to_profile(request)


'''
    Upload Picture
'''


def upload_picture(request):
    if request.method == 'GET':
        return render(request, 'core/upload_picture.html')

    if request.method == 'POST':
        UserLogic.upload_picture(request)
        return UserLogic.redirect_to_profile(request)


'''
    Logout
'''


def logout(request):
    auth.logout(request)
    return redirect('core:home')


'''
    Update Information
'''


def update_basic_information(request):
    if request.method == 'POST':
        information = UserInformation(request.POST)

        if information.is_valid(request=request):
            user = request.user
            user.location = request.POST.get('location')
            user.biography = request.POST.get('basic_information')
            user.hair_type = request.POST.get('hair_type')
            user.email = request.POST.get('email')
            user.phone_number = request.POST.get('phone_number')
            user.save()
            return UserLogic.redirect_to_profile(request)
        else:
            request.session['information_errors'] = information.errors
            return redirect('core:update_basic_information')

    if request.method == 'GET':
        if 'information_errors' in request.session:
            errors = request.session['information_errors']

        else:
            errors = None

        request.session['information_errors'] = None
        return render(request, 'core/basic_information.html', {'user': request.user, 'errors': errors})


def change_password(request):
    if not request.user.is_anonymous:
        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            new_password_repeat = request.POST.get('new_password_repeat')

            if new_password == new_password_repeat:
                request.user.set_password(new_password)
                request.user.save()
                auth.login(request, request.user)
                return UserLogic.redirect_to_profile(request)
            else:
                request.session['password_error'] = "Passwords don't match."
                return redirect('core:change_password')

        if request.method == 'GET':
            if 'password_error' in request.session:
                password_error = request.session.get('password_error')
            else:
                password_error = None
            request.session['password_error'] = None
            return render(request, 'core/change_password.html', {'password_error': password_error})
    else:
        return redirect('core:logout')

'''
    NAV BAR
'''


def home(request):
    return render(request, 'core/home/home_home.html')


def home_style(request):
    return render(request, 'core/home/home_findyourstyle.html')


def home_stylist(request):
    return render(request, 'core/home/home_becomeastylist.html')


def home_login(request):
    if not request.user.is_anonymous:
        return UserLogic.redirect_to_profile(request)

    if 'error' in request.session:
        error = request.session['error']

    else:
        error = None
    request.session['error'] = None

    return render(request, 'core/home/home_login.html', {'error': error})


def home_safety(request):
    return render(request, 'core/home/home_safety.html')
