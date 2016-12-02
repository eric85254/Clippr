from django.conf.urls import url

from core import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'create_new_user/$', views.entering_user, name="user_authentication"),
    url(r'returning_user/$', views.returning_user, name="returning_user"),
    url(r'upload_picture/$', views.upload_picture, name="upload_picture")
]
