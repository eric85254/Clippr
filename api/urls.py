from django.conf.urls import url, include
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'appointment', views.AppointmentsViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]