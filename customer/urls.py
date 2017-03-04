from django.conf.urls import url, include

from customer import views

create_appointment_patterns = [
    url(r'^$', views.create_appointment, name="create_appointment"),
    url(r'^stylist_search/$', views.stylist_search, name="stylist_search"),
    url(r'^catch_menu_choices/$', views.catch_menu_choices, name="catch_menu_choices"),
    url(r'^obtain_selected_haircut/$', views.obtain_selected_haircut,
        name='obtain_selected_haircut'),
    url(r'^obtain_stylist_profile/$', views.obtain_stylist_profile, name='obtain_stylist_profile'),
    url(r'^obtain_selected_menuOption/$', views.obtain_selected_menuOption, name='obtain_selected_menuOption')
]

appointment_modifiers = [
    url(r'^$', views.dashboard, name="dashboard"),
    url(r'^appointment/cancel_appointment/$', views.cancel_appointment, name='cancel_appointment'),
    url(r'^appointment/reschedule_appointment/$', views.reschedule_appointment, name='reschedule_appointment'),
    url(r'^appointment/accept_appointment/$', views.accept_appointment, name='accept_appointment'),
    url(r'^view_bill/$', views.view_bill, name='view_bill')
]

urlpatterns = [
    url(r'^profile/$', views.profile, name="profile"),
    url(r'^dashboard/', include(appointment_modifiers)),
    url(r'^create_appointment/', include(create_appointment_patterns)),
    url(r'^become_stylist/$', views.become_stylist, name="become_stylist"),
    url(r'^submit_review/$', views.submit_review, name="submit_review")
]
