"""
    These views are for the custom administration page. They are used to schedule interviews and approve new stylists.
    To access this page the user must be a super user. (This requirement should eventually be downgraded to staff).
"""
from datetime import datetime

from django.shortcuts import render, redirect

# Create your views here.
from core.models import Application


def profile(request):
    """
        METHODS ALLOWED = [GET]

        This view redirects the user to the administration profile/home page.
    """
    if request.user.is_superuser:
        return render(request, 'administration/profile.html')
    else:
        return redirect('core:logout')


def view_stylist_applications(request):
    """
        METHODS ALLOWED = [GET]

        Pulls all the applications with the status *PENDING* and renders the view page.
    """
    if request.user.is_superuser:
        applications = Application.objects.filter(application_status="PENDING")
        return render(request, 'administration/unread_applications.html', {'applications': applications})
    else:
        return redirect('core:logout')


def schedule_interview(request):
    """
        METHODS ALLOWED = [POST]

        Allows the staff to schedule an interview with a potential stylist.

        | First the correct application is pulled using the *application_id* sent via POST
        | Next the interview_time is set by stripping the date string sent via POST
        | The application_status is modified to *SCHEDULED* and finally saved.

        The user is redirected to the page they were originally on.
    """
    if request.user.is_superuser:
        if request.method == 'POST':
            application = Application.objects.get(pk=int(request.POST.get('application_id')))
            application.interview_time = datetime.strptime(request.POST.get('date'), '%Y-%m-%dT%H:%M')
            application.application_status = "SCHEDULED"
            application.save()
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect("core:logout")


def view_interviews(request):
    """
        METHODS ALLOWED = [GET]

        Renders all applications with the application_status of *SCHEDULED*
    """
    # ToDo: Separate applicants into upcoming interviews and passed interviews. Only give the passed interviews the option of 'approval'.
    if request.user.is_superuser:
        applications = Application.objects.filter(application_status="SCHEDULED")
        return render(request, 'administration/view_interviews.html', {'applications': applications})
    else:
        return redirect('core:logout')


def view_rejects(request):
    """
        METHODS ALLOWED = [GET]

        Renders all applications with the application_status of *REJECTED*
    """
    if request.user.is_superuser:
        applications = Application.objects.filter(application_status='REJECTED')
        return render(request, 'administration/view_rejects.html', {'applications': applications})
    else:
        return redirect('core:logout')


def reinstate_application(request):
    # noinspection PyUnresolvedReferences
    """
        METHODS ALLOWED = [POST]

        - **Post Params:**
            :param application_id: utlized to obtain the correct application from the database

        The application_status is updated to *PENDING*
    """
    if request.user.is_superuser:
        if request.method == 'POST':
            application = Application.objects.get(pk=int(request.POST.get('application_id')))
            application.application_status = 'PENDING'
            application.save()
        return redirect('administration:view_rejects')
    else:
        return redirect('core:logout')


def reject_applicant(request):
    """
        METHODS ALLOWED = [POST]

        - **Post Params:**
            :param application_id: utilized to obtain the correct application from the database
            :param denied_reason: reason why application was denied

        | The correct application is pulled.
        | The status is updated to *REJECTED*
        | The denied_reason field is filled
        | The application is saved
        |
        | The applicant is pulled from the application and the is_stylist field is changed to NO
        | The applicant is saved
        |
        | User is redirected to their prior page.
    """
    if request.user.is_superuser:
        if request.method == 'POST':
            application = Application.objects.get(pk=int(request.POST.get('application_id')))
            application.application_status = 'REJECTED'
            application.denied_reason = request.POST.get('denied_reason')
            application.save()

            application.applicant.is_stylist = 'NO'
            application.applicant.save()
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('core:logout')


def approve_applicant(request):
    """
        METHODS ALLOWED = [POST]

        - **Post Params:**
            :param application_id: utilized to obtain the correct application from the database

        | The correct application is pulled
        | Status is updated to *APPROVED*
        | Application is saved

        | Applicant is pulled from the Application
        | Applicant's is_stylist field is changed to YES
        | Applicant is saved
    """
    if request.user.is_superuser:
        if request.method == 'POST':
            application = Application.objects.get(pk=int(request.POST.get('application_id')))
            application.application_status = 'APPROVED'
            application.save()

            application.applicant.is_stylist = 'YES'
            application.applicant.save()
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('core:logout')


def view_stylists(request):
    """
        METHODS ALLOWED = [GET]

        Applications with the status *APPROVED* are rendered.
    """
    if request.user.is_superuser:
        applications = Application.objects.filter(application_status='APPROVED')
        return render(request, 'administration/view_stylists.html', {'applications': applications})
    else:
        return redirect('core:logout')
