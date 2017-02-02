from django.contrib import auth
from django.http import JsonResponse
from django.shortcuts import render, redirect

from core.forms import NewUserForm
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

        else:
            print(create_user_form.errors)
            data = create_user_form.errors
            data['success'] = False
            return JsonResponse(data=data)

'''
    Returning User
'''

def returning_user(request):
    if request.method == 'GET':
        return redirect('core:home')

    if request.method == 'POST':
        user = UserLogic.retrieve_user(request)
        UserLogic.login(request, user)
        return UserLogic.redirect_to_profile(user)

'''
    Upload Picture
'''

def upload_picture(request):
    if request.method == 'GET':
        return render(request, 'core/upload_picture.html')

    if request.method == 'POST':
        UserLogic.upload_picture(request)
        return UserLogic.redirect_to_profile(request.user)

'''
    Logout
'''

def logout(request):
    auth.logout(request)
    return redirect('core:home')

'''
    Home
'''

def home(request):
    return render(request, 'core/home/home_core.html')

'''
    Update Basic Information
'''

def update_basic_information(request):
    if request.method == 'POST':
        UserLogic.update_basic_information(request)
        return UserLogic.redirect_to_profile(request.user)

    if request.method == 'GET':
        return redirect(request.META.get('HTTP_REFERER'))

    # else:
    #     if request.user.is_stylist == 'YES':
    #         stylist = request.user
    #         return render(request, 'core/basic_information.html', {'user': stylist})
    #     else:
    #         customer = request.user
    #         return render(request, 'core/basic_information.html', {'user': customer})
