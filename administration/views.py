import datetime

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


def schedule_interview(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            application = Applications.objects.get(pk=int(request.POST.get('application_id')))
            if 'schedule' in request.POST:
                application.interview_time = datetime.datetime.now()
                application.application_status = "SCHEDULED"
                application.save()
            elif 'reject' in request.POST:
                application.application_status = "REJECTED"
                application.save()
        return redirect("administration:view_interviews")
    else:
        return redirect("core:logout")


def view_interviews(request):
    if request.user.is_superuser:
        applications = Applications.objects.filter(interview_time__isnull=False)
        return render(request, 'administration/view_interviews.html', {'applications': applications})
    else:
        return redirect('core:logout')


def view_rejects(request):
    if request.user.is_superuser:
        applications = Applications.objects.filter(application_status="REJECTED")
        return render(request, 'administration/view_rejects.html', {'applications': applications})
    else:
        return redirect('core:logout')


def reinstate_application(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            application = Applications.objects.get(pk=int(request.POST.get('application_id')))
            application.application_status = 'PENDING'
            application.save()
        return redirect('administration:view_rejects')
    else:
        return redirect('core:logout')