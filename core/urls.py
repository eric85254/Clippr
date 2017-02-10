from django.conf.urls import url, include

from core import views

loginpatterns = [
    url(r'^$', views.home_login, name="home_login"),
    url(r'^create_user/$', views.create_user, name="create_user"),
    url(r'^returning_user/$', views.returning_user, name="returning_user"),
]

navbarpatterns = [
    url(r'^$', views.home, name="index"),
    url(r'^home/$', views.home, name="home"),
    url(r'^login/', include(loginpatterns)),
    url(r'^stylist/$', views.home_stylist, name="home_stylist"),
    url(r'^style/$', views.home_style, name="home_style"),
    url(r'^safety/$', views.home_safety, name="home_safety"),
]

profilepatterns = [
    url(r'^upload_picture/$', views.upload_picture, name="upload_picture"),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^update_basic_information/$', views.update_basic_information, name="update_basic_information")
]

urlpatterns = [
    url(r'^', include(navbarpatterns)),
    url(r'^profile/', include(profilepatterns)),
]
