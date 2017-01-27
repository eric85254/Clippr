from django.shortcuts import render, redirect

from core.models import Appointment
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
        if Appointment.objects.filter(stylist=request.user).exists():
            appointment_list = Appointment.objects.filter(stylist=request.user)

        else:
            appointment_list = None
        return render(request, 'stylist/dashboard.html', {'full_name': request.user.get_full_name(),
                                                          'appointments': appointment_list})
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
                new_portfolioHaircut.save()

            return redirect('stylist:profile')
        else:
            return render(request, 'stylist/upload_haircut.html')

    else:
        return redirect('core:logout')