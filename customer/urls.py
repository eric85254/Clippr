from django.conf.urls import url

from customer import views

urlpatterns = [
    url(r'profile/$', views.profile, name="profile"),
    url(r'dashboard/$', views.dashboard, name="dashboard"),
    url(r'create_appointment/$', views.create_appointment, name="create_appointment"),
    url(r'stylist_search/$', views.stylist_search, name="stylist_search"),
    url(r'become_stylist/$', views.become_stylist, name="become_stylist")
]
