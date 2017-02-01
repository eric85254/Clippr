from django.shortcuts import render, redirect

from core.models import Appointment, Menu
from stylist.forms import NewPortfolioHaircutForm
from stylist.models import PortfolioHaircut


def profile(request):
    if request.user.is_stylist == 'YES':
        full_name = request.user.get_full_name()

        portfolio_haircuts = PortfolioHaircut.objects.filter(stylist=request.user)

        return render(request, 'stylist/profile.html',
                      {'full_name': full_name,
                       'stylist': request.user,
                       'portfolio_haircuts': portfolio_haircuts},)
    else:
        return redirect('core:logout')

def dashboard(request):
    if request.user.is_stylist == 'YES':
        pending_appointments = Appointment.objects.filter(stylist=request.user, status=Appointment.STATUS_PENDING)
        accepted_appointments = Appointment.objects.filter(stylist=request.user, status=Appointment.STATUS_ACCEPTED)
        declined_appointments = Appointment.objects.filter(stylist=request.user, status=Appointment.STATUS_DECLINED)
        return render(request, 'stylist/dashboard.html', {'full_name': request.user.get_full_name(),
                                                          'pending_appointments': pending_appointments,
                                                          'accepted_appointments': accepted_appointments,
                                                          'declined_appointments': declined_appointments})
    else:
        return redirect('core:logout')

def upload_haircut(request):
    if request.user.is_stylist == 'YES':
        if request.method == 'POST':
            new_portfolioHaircut_form = NewPortfolioHaircutForm(request.POST)

            if new_portfolioHaircut_form.is_valid():
                new_portfolioHaircut = new_portfolioHaircut_form.save(commit=False)
                new_portfolioHaircut.stylist = request.user
                new_portfolioHaircut.picture = request.FILES['picture']
                # Finding and adding selected menu option to new_portfolioHaircut
                if request.POST.get('menu_main') == 'none':
                    menu_main = None
                else:
                    menu_main = Menu.objects.filter(category__icontains='main').get(name=request.POST.get('menu_main'))
                new_portfolioHaircut.menu_option = menu_main
                new_portfolioHaircut.save()

            return redirect('stylist:profile')
        else:
            return render(request, 'stylist/upload_haircut.html')

    else:
        return redirect('core:logout')


def accept_appointment(request):
    if request.user.is_stylist == 'YES':
        if request.method == 'POST':
            appointment = Appointment.objects.get(pk=request.POST.get('appointment_pk'))
            appointment.status = Appointment.STATUS_ACCEPTED
            appointment.save()
    return redirect(request.META.get('HTTP_REFERER'))


def decline_appointment(request):
    if request.user.is_stylist == 'YES':
        if request.method == 'POST':
            appointment = Appointment.objects.get(pk=request.POST.get('appointment_pk'))
            appointment.status = Appointment.STATUS_DECLINED
            appointment.save()
    return redirect(request.META.get('HTTP_REFERER'))