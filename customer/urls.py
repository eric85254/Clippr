from django.conf.urls import url

from customer import views

urlpatterns = [
    url(r'profile/$', views.profile, name="profile"),
    url(r'dashboard/$', views.dashboard, name="dashboard")
]
