from django.conf.urls import url, include
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'appointment', views.AppointmentViewSet)
router.register(r'haircut', views.HaircutViewSet)
router.register(r'stylist', views.StylistViewSet, 'stylist')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'user_login/$', views.user_login),
    url(r'stylist_search/(?P<search>.*)$', views.stylist_search),
]