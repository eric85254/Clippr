from django.conf.urls import url
from administration import views

# ToDo: Interesting Error.. if the url name for views.profile is r'home/$' it redirects to the actual home page and
# does not go to views.profile. Figure this out.
urlpatterns = [
    url(r'profile/$', views.profile, name="profile"),
    url(r'view_stylist_applications', views.view_stylist_applications, name="view_stylist_applications"),
    url(r'schedule_interview', views.schedule_interview, name="schedule_interview"),
    url(r'view_interviews', views.view_interviews, name="view_interviews")
]
