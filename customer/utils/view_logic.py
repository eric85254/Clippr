from django.shortcuts import render, redirect

from core.models import Appointment, Application


class CustomerLogic(object):
    @staticmethod
    def retrieve_application(request):
        if len(Application.objects.filter(applicant=request.user)) > 0:
            return Application.objects.get(applicant=request.user)
        else:
            return False

    @staticmethod
    def is_customer(request):
        if request.user.is_stylist == 'NO':
            return True
        else:
            return False

    @classmethod
    def render_dashboard(cls, request):
        if cls.is_customer(request):
            pending_appointments = Appointment.objects.filter(stylist=request.user, status=Appointment.STATUS_PENDING)
            accepted_appointments = Appointment.objects.filter(stylist=request.user, status=Appointment.STATUS_ACCEPTED)
            declined_appointments = Appointment.objects.filter(stylist=request.user, status=Appointment.STATUS_DECLINED)
            rescheduled_bystylist_appointments = Appointment.objects.filter(stylist=request.user,
                                                                            status=Appointment.STATUS_RECHEDULED_BYSTYLIST)
            completed_appointments = Appointment.objects.filter(stylist=request.user,
                                                                status=Appointment.STATUS_COMPLETED)
            return render(request, 'customer/dashboard.html', {'full_name': request.user.get_full_name(),
                                                               'pending_appointments': pending_appointments,
                                                               'accepted_appointments': accepted_appointments,
                                                               'declined_appointments': declined_appointments,
                                                               'rescheduled_bystylist_appointments': rescheduled_bystylist_appointments,
                                                               'completed_appointments': completed_appointments})
        else:
            return redirect('core:logout')

    @classmethod
    def render_application_status(cls, request):
        if cls.is_customer(request):
            application = cls.retrieve_application(request)

            if application:
                if application.application_status == 'PENDING':
                    return render(request, 'customer/stylistApplications/application_submitted.html')
                elif application.application_status == 'SCHEDULED':
                    return render(request, 'customer/stylistApplications/interview_scheduled.html',
                                  {'application': application})
                elif application.application_status == 'REJECTED':
                    return render(request, 'customer/stylistApplications/application_rejected.html')

            else:
                return render(request, 'customer/stylistApplications/become_stylist.html')

        else:
            return redirect('core:logout')
