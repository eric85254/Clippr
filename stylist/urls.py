from django.conf.urls import url

from stylist import views

urlpatterns = [
    url(r'profile/$', views.profile, name="profile"),
    url(r'dashboard/$', views.dashboard, name="dashboard"),
    url(r'upload_haircut/$', views.upload_haircut, name="upload_haircut"),
    url(r'accept_appointment/$', views.accept_appointment, name='accept_appointment'),
    url(r'decline_appointment/$', views.decline_appointment, name='decline_appointment'),
    url(r'reschedule_appointment/$', views.reschedule_appointment, name='reschedule_appointment'),
    url(r'view_bill/$', views.view_bill, name='view_bill'),
    url(r'delete_item/$', views.delete_item, name='delete_item'),
    url(r'add_item/$', views.add_item, name='add_item'),
    url(r'edit_portfoliohaircut/$', views.edit_portfoliohaircut, name='edit_portfoliohaircut')
]
