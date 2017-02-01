from django.conf.urls import url

from stylist import views

urlpatterns = [
    url(r'profile/$', views.profile, name="profile"),
    url(r'dashboard/$', views.dashboard, name="dashboard"),
    url(r'upload_haircut/$', views.upload_haircut, name="upload_haircut"),
    url(r'accept_appointment/$', views.accept_appointment, name='accept_appointment'),
    url(r'decline_appointment/$', views.decline_appointment, name='decline_appointment')
]
