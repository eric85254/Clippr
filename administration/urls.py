from django.conf.urls import url
from administration import views

# ToDo: Interesting Error.. if the url name for views.profile is r'home/$' it redirects to the actual home page and
# does not go to views.profile. Figure this out.
urlpatterns = [
    url(r'profile/$', views.profile, name="profile"),
    url(r'view_stylist_applications/$', views.view_stylist_applications, name="view_stylist_applications"),
    url(r'schedule_interview/$', views.schedule_interview, name="schedule_interview"),
    url(r'view_interviews/$', views.view_interviews, name="view_interviews"),
    url(r'view_rejects/$', views.view_rejects, name="view_rejects"),
    url(r'reinstate_application/$', views.reinstate_application, name="reinstate_application"),
    url(r'reject_applicant/$', views.reject_applicant, name="reject_applicant"),
    url(r'approve_applicant/$', views.approve_applicant, name="approve_applicant"),
    url(r'view_stylists/$', views.view_stylists, name="view_stylists")
]
