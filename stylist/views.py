from django.shortcuts import render, redirect

from stylist.models import Appointment


def profile(request):
    if request.user.is_stylist == 'YES':
        full_name = request.user.get_full_name()
        if request.user.profile_picture is not None:
            stylist = request.user
        else:
            stylist = None
        return render(request, 'stylist/profile.html',
                      {'full_name': full_name,
                       'stylist': stylist})
    else:
        return redirect('core:logout')

def dashboard(request):
    if request.user.is_stylist == 'YES':
        if Appointment.objects.filter(stylist=request.user).exists():
            appointment_list = Appointment.objects.filter(stylist=request.user)

        else:
            appointment_list = None
        return render(request, 'stylist/dashboard.html', {'full_name': request.user.get_full_name(),
                                                          'appointments': appointment_list})
    else:
        return redirect('core:logout')