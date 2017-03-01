from django.conf.urls import url, include

from stylist import views

appointmentpatterns = [
    url(r'^accept_appointment/$', views.accept_appointment, name='accept_appointment'),
    url(r'^decline_appointment/$', views.decline_appointment, name='decline_appointment'),
    url(r'^reschedule_appointment/$', views.reschedule_appointment, name='reschedule_appointment'),
    url(r'^complete_appointment/$', views.complete_appointment, name='complete_appointment'),
    url(r'^submit_review/$', views.submit_review, name='submit_review'),
]

billpatterns = [
    url(r'^view_bill/$', views.view_bill, name='view_bill'),
    url(r'^delete_item/$', views.delete_item, name='delete_item'),
    url(r'^add_item/$', views.add_item, name='add_item'),
    url(r'^add_haircut/$', views.add_haircut, name='add_haircut'),
    url(r'^add_travel_fee/$', views.add_travel_fee, name='add_travel_fee')
]

profilepatterns = [
    url('^$', views.profile, name="profile"),
    url(r'^upload_haircut/$', views.upload_haircut, name="upload_haircut"),
    url(r'^test/$', views.profile_test, name='profile_test')
]

portfoliopatterns = [
    url('^$', views.portfolio, name="portfolio"),
    url(r'^edit_portfoliohaircut/$', views.edit_portfoliohaircut, name='edit_portfoliohaircut'),
    url(r'^delete_portfoliohaircut/$', views.delete_portfoliohaircut, name='delete_portfoliohaircut')
]

menupatterns = [
    url(r'^select_menu_option/$', views.select_menu_option, name="select_menu_option"),
    url(r'^remove_menu_option/$', views.remove_menu_option, name="remove_menu_option"),
    url(r'^create_menu_option/$', views.create_menu_option, name="create_menu_option"),
    url(r'^edit_menu_option/$', views.edit_menu_option, name="edit_menu_option"),
    url(r'^delete_menu_option/$', views.delete_menu_option, name="delete_menu_option")
]

urlpatterns = [
    url(r'^profile/', include(profilepatterns)),
    url(r'^dashboard/$', views.dashboard, name="dashboard"),
    url(r'^appointment/', include(appointmentpatterns)),
    url(r'^appointment/bill/', include(billpatterns)),
    url(r'^transactions/$', views.transactions, name="transactions"),
    url(r'^portfolio/', include(portfoliopatterns)),
    url(r'^profile_test/', include(profilepatterns)),
    url(r'^menu/', include(menupatterns)),
    url(r'^appointments/', views.appointments, name="appointments")
]
