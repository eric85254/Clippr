from django.conf.urls import url

from core import views

urlpatterns = [
    url(r'^$', views.home, name="index"),
    url(r'^home/$', views.home, name="home"),
    url(r'^login/$', views.home_login, name="home_login"),
    url(r'^stylist/$', views.home_stylist, name="home_stylist"),
    url(r'^style/$', views.home_style, name="home_style"),
    url(r'^safety/$', views.home_safety, name="home_safety"),
    url(r'^create_user/$', views.create_user, name="create_user"),
    url(r'^returning_user/$', views.returning_user, name="returning_user"),
    url(r'^upload_picture/$', views.upload_picture, name="upload_picture"),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^update_basic_information/$', views.update_basic_information, name="update_basic_information")
]
