from django.conf.urls import url

from customer import views

urlpatterns = [
    url(r'profile/$', views.profile, name="profile"),
    url(r'dashboard/$', views.dashboard, name="dashboard"),
    url(r'create_appointment/$', views.create_appointment, name="create_appointment"),
    url(r'stylist_search/$', views.stylist_search, name="stylist_search"),
    url(r'become_stylist/$', views.become_stylist, name="become_stylist"),
    url(r'catch_menu_choices/$', views.catch_menu_choices, name="catch_menu_choices"),
    url(r'create_appointment_obtainStylistUsername', views.create_appointment_obtainStylistUsername, name='create_appointment_obtainStylistUsername'),
    url(r'create_appointment_menuMainChoice', views.create_appointment_menuMainChoice, name='create_appointment_menuMainChoice')
]
