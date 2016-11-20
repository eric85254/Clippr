from django.conf.urls import url

from core import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'create_new_user/$', views.create_new_user, name="create_new_user")
]
