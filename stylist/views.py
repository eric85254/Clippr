from django.shortcuts import render

from stylist.models import Appointments


def profile(request):
    full_name = request.user.get_full_name()
    if request.user.profile_picture is not None:
        stylist = request.user
    else:
        stylist = None
    return render(request, 'stylist/profile.html',
                  {'full_name': full_name,
                   'stylist': stylist})


def dashboard(request):
    if Appointments.objects.filter(stylist=request.user).exists():
        appointment_list = Appointments.objects.filter(stylist=request.user)

    else:
        appointment_list = None
    return render(request, 'stylist/dashboard.html', {'full_name': request.user.get_full_name(),
                                                      'appointments': appointment_list})
