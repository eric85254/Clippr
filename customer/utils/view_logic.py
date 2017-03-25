"""
    Contains logic that is used throughout the Customer app.
    @classmethods allow you to utilize the @staticmethods of the class.
"""
from django.shortcuts import render, redirect

from core.models import Appointment, Application, Review
from stylist.utils.view_logic import BillLogic


class CustomerLogic(object):
    # Todo: This is kind of useless.
    @staticmethod
    def retrieve_application(request):
        if len(Application.objects.filter(applicant=request.user)) > 0:
            return Application.objects.get(applicant=request.user)
        else:
            return False

    # Todo: This is great! Why don't you use this code everywhere. It'll save you a lot of hassle if you want to switch to booleans.
    @staticmethod
    def is_customer(request):
        if request.user.is_stylist == 'NO':
            return True
        else:
            return False

    @classmethod
    def render_dashboard(cls, request):
        """
            This is here because I hate seeing this god awful chunk of code within the views.py
            It just pulls all the appointments by status and the reviews and renders them on the dashboard.
        """
        if cls.is_customer(request):
            pending_appointments = Appointment.objects.filter(customer=request.user, status=Appointment.STATUS_PENDING)
            accepted_appointments = Appointment.objects.filter(customer=request.user,
                                                               status=Appointment.STATUS_ACCEPTED)
            declined_appointments = Appointment.objects.filter(customer=request.user,
                                                               status=Appointment.STATUS_DECLINED)
            rescheduled_bystylist_appointments = Appointment.objects.filter(customer=request.user,
                                                                            status=Appointment.STATUS_RECHEDULED_BYSTYLIST)
            rescheduled_bycustomer_appointments = Appointment.objects.filter(customer=request.user,
                                                                             status=Appointment.STATUS_RESCHEDULED_BYCUSTOMER)
            completed_appointments = Appointment.objects.filter(customer=request.user,
                                                                status=Appointment.STATUS_COMPLETED)
            pending_appointments_bill = BillLogic.combine_appointment_bill(pending_appointments)
            accepted_appointments_bill = BillLogic.combine_appointment_bill(accepted_appointments)
            completed_appointments_bill = BillLogic.combine_appointment_bill(completed_appointments)

            incomplete_reviews = Review.objects.filter(stylist_rating__isnull=True)
            complete_reviews = Review.objects.filter(stylist_rating__isnull=False, customer_rating__isnull=False)
            return render(request, 'customer/customerReal/dashboard/dashboard_core.html',
                          {'full_name': request.user.get_full_name(),
                           # 'pending_appointments': pending_appointments,
                           # 'accepted_appointments': accepted_appointments,
                           # 'completed_appointments': completed_appointments,
                           'pending_appointments_bill': pending_appointments_bill,
                           'accepted_appointments_bill': accepted_appointments_bill,
                           'completed_appointments_bill': completed_appointments_bill,
                           'incomplete_reviews': incomplete_reviews,
                           'complete_reviews': complete_reviews})
        else:
            return redirect('core:logout')

    # todo: shouldn't have this here.
    @classmethod
    def render_application_status(cls, request):
        """
            Shouldn't really be here either. Just renders the correct application_status.
        """
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
