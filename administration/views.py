from django.shortcuts import render, redirect


# Create your views here.
from stylist.models import Applications


def profile(request):
    if request.user.is_superuser:
        return render(request, 'administration/profile.html')
    else:
        return redirect('core:logout')

def view_stylist_applications(request):
    if request.user.is_superuser:
        applications = Applications.objects.filter(application_status="PENDING")
        return render(request, 'administration/unread_applications.html', {'applications': applications})
    else:
        return redirect('core:logout')