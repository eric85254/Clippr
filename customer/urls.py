"""
    Urls of the customer app

    Organized by the following categories
        | create_appointment_patterns
        | appointment_modifiers
        | urlpatterns
"""
from django.conf.urls import url, include

from customer import views

create_appointment_patterns = [
    url(r'^$', views.create_appointment, name="create_appointment"),
    url(r'^stylist_search/$', views.stylist_search, name="stylist_search"),
    url(r'^obtain_selected_haircut/$', views.obtain_selected_haircut,
        name='obtain_selected_haircut'),
    url(r'^obtain_stylist_profile/$', views.obtain_stylist_profile, name='obtain_stylist_profile'),
    url(r'^obtain_selected_menuOption/$', views.obtain_selected_menuOption, name='obtain_selected_menuOption')
]

calendar_patterns = [
    url(r'^schedule_appointment/$', views.schedule_appointment, name="schedule_appointment")
]

appointment_patterns = [
    url(r'^$', views.appointments, name="appointments"),
    url(r'^cancel_appointment/$', views.cancel_appointment, name='cancel_appointment'),
    url(r'^reschedule_appointment/$', views.reschedule_appointment, name='reschedule_appointment'),
    url(r'^accept_appointment/$', views.accept_appointment, name='accept_appointment'),
]

appointment_modifiers = [
    url(r'^$', views.dashboard, name="dashboard"),
    url(r'^appointment/', include(appointment_patterns)),
    url(r'^view_bill/$', views.view_bill, name='view_bill'),
    url(r'^calendar/', include(calendar_patterns))
]


search_for_thesis = [
    url(r'^$', views.search_core, name="search_core"),
    url(r'^render_stylist_data/$', views.render_stylist_data, name="render_stylist_data"),
    url(r'^save_haircut/$', views.save_haircut, name="save_haircut"),
    url(r'^save_menu/$', views.save_menu, name="save_menu"),
    url(r'^appointment_calendar/$', views.reveal_fullcalendar, name="reveal_fullcalendar"),
]

urlpatterns = [
    url(r'^profile/$', views.profile, name="profile"),
    url(r'^dashboard/', include(appointment_modifiers)),
    url(r'^create_appointment/', include(create_appointment_patterns)),
    url(r'^become_stylist/$', views.become_stylist, name="become_stylist"),
    url(r'^submit_review/$', views.submit_review, name="submit_review"),

    #for thesis
    url(r'^search/', include(search_for_thesis))
]
