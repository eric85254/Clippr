from django.conf.urls import url, include

from customer import views

create_appointment_patterns = [
    url(r'^$', views.create_appointment, name="create_appointment"),
    url(r'^stylist_search/$', views.stylist_search, name="stylist_search"),
    url(r'^catch_menu_choices/$', views.catch_menu_choices, name="catch_menu_choices"),
    # Not sure if obtain_stylist_username is actually used.
    # ToDo: Find out whether obtainstylistUsername is actually used.
    url(r'^obtain_stylist_username/$', views.create_appointment_obtainStylistUsername,
        name='create_appointment_obtainStylistUsername'),
    url(r'^obtain_menu_choice/$', views.create_appointment_menuMainChoice,
        name='create_appointment_menuMainChoice'),
    url(r'^obtain_stylist_profile/$', views.obtain_stylist_profile, name='obtain_stylist_profile'),
]

appointment_modifiers = [
    url(r'^$', views.dashboard, name="dashboard"),
    url(r'^appointment/cancel_appointment/$', views.cancel_appointment, name='cancel_appointment'),
    url(r'^appointment/reschedule_appointment/$', views.reschedule_appointment, name='reschedule_appointment'),
    url(r'^appointment/accept_appointment/$', views.accept_appointment, name='accept_appointment')
]

urlpatterns = [
    url(r'^profile/$', views.profile, name="profile"),
    url(r'^dashboard/', include(appointment_modifiers)),
    url(r'^create_appointment/', include(create_appointment_patterns)),
    url(r'^become_stylist/$', views.become_stylist, name="become_stylist"),
    url(r'^submit_review/$', views.submit_review, name="submit_review")
]
