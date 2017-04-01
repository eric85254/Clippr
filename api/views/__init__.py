from api.views.UserViews import UserViewSet, user_login, user_logout
from api.views.StylistViews import stylist_search, StylistViewSet
from api.views.RatingViews import customer_rating, stylist_rating
from api.views.AppointmentViews import AppointmentViewSet, CalendarEventViewSet, exclude_date, ShiftViewSet
from api.views.PortfolioHaircutViews import HaircutViewSet
from api.views.MenuViews import StylistMenuViewSet, GlobalMenuViewSet
from api.views.CustomerViews import CustomerViewSet