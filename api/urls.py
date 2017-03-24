"""
    The Urls from the ViewSets are registered through a router. Standalone method views are manually registered through urlpatterns.
    The manually registered views (in url patterns) don't show up in the home page of /api.
"""
from django.conf.urls import url, include
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet, 'user')
router.register(r'appointment', views.AppointmentViewSet)
router.register(r'haircut', views.HaircutViewSet)
router.register(r'stylist', views.StylistViewSet, 'stylist')
router.register(r'global_menu', views.GlobalMenuViewSet)
router.register(r'stylist_menu', views.StylistMenuViewSet)
router.register(r'shift', views.ShiftViewSet)
router.register(r'calendar_event', views.CalendarEventViewSet, 'calendarevent')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^user_login/$', views.user_login),
    url(r'^user_logout/$', views.user_logout),
    url(r'^stylist_search/(?P<search>.*)$', views.stylist_search),
    url(r'^customer_rating/(?P<customer_pk>.*)$', views.customer_rating),
    url(r'^stylist_rating/(?P<stylist_pk>.*)$', views.stylist_rating)
]