from django.conf.urls import url

from core import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'home/$', views.home, name="home"),
    url(r'create_user/$', views.create_user, name="create_user"),
    url(r'returning_user/$', views.returning_user, name="returning_user"),
    url(r'upload_picture/$', views.upload_picture, name="upload_picture"),
    url(r'logout/$', views.logout, name="logout"),
    url(r'basic_information/$', views.basic_information, name="basic_information")
]
