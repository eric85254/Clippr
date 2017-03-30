from core.models import Appointment

appointment_information = [
    {
        'status': Appointment.STATUS_PENDING,
        'start_date_time': '2017-04-07T12:00',
    },
    {
        'status': Appointment.STATUS_RECHEDULED_BYSTYLIST,
        'start_date_time': '2017-04-04T12:00',
    },
    {
        'status': Appointment.STATUS_RESCHEDULED_BYCUSTOMER,
        'start_date_time': '2017-04-05T12:00',
    },
    {
        'status': Appointment.STATUS_ACCEPTED,
        'start_date_time': '2017-04-06T12:00',
    },
    {
        'status': Appointment.STATUS_DECLINED,
        'start_date_time': '2017-04-03T12:00',
    },
    {
        'status': Appointment.STATUS_COMPLETED,
        'start_date_time': '2017-04-03T12:00',
    },
]
