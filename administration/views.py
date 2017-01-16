from datetime import datetime

from django.shortcuts import render, redirect


# Create your views here.
from core.models import User
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
            application.interview_time = datetime.strptime(request.POST.get('date'), '%Y-%m-%dT%H:%M')
            application.application_status = "SCHEDULED"
            application.save()
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect("core:logout")


def view_interviews(request):
    # ToDo: Separate applicants into upcoming interviews and passed interviews. Only give the passed interviews the option of 'approval'.
    if request.user.is_superuser:
        applications = Applications.objects.filter(application_status="SCHEDULED")
        return render(request, 'administration/view_interviews.html', {'applications': applications})
    else:
        return redirect('core:logout')


def view_rejects(request):
    if request.user.is_superuser:
        applications = Applications.objects.filter(application_status='REJECTED')
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


def reject_applicant(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            application = Applications.objects.get(pk=int(request.POST.get('application_id')))
            application.application_status = 'REJECTED'
            application.denied_reason = request.POST.get('denied_reason')
            application.save()

            application.applicant.is_stylist = 'NO'
            application.applicant.save()
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('core:logout')


def approve_applicant(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            application = Applications.objects.get(pk=int(request.POST.get('application_id')))
            application.application_status = 'APPROVED'
            application.save()

            application.applicant.is_stylist = 'YES'
            application.applicant.save()
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('core:logout')


def view_stylists(request):
    if request.user.is_superuser:
        applications = Applications.objects.filter(application_status='APPROVED')
        return render(request, 'administration/view_stylists.html', {'applications': applications})
    else:
        return redirect('core:logout')