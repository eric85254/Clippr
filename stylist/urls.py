from django.conf.urls import url

from stylist import views

urlpatterns = [
    url(r'profile/$', views.profile, name="profile")
]
