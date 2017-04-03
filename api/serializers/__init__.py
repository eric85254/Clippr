
"""
    Consider this example: When the webpage receives data for a stylist it is ideal to also receive information about
    the stylist's portfolio and the stylist's menu options. However, both the portfolio and the menu options are stored
    in a separate model. So to pull that information, a serializer for each model needs to be created. These serializers
    should then be included within the Stylist serializer.

    | Now we've essentially created a nested serializer. When running the server, an error will appear if the PortfolioSerializer
    and the MenuSerializers are not defined before their usage in the StylistSerializer. This becomes problematic when
    dealing with numerous nested serializers, and developers will spend more time working on organization rather then code.
    For this reason, the serializers were abstracted to their individual classes and simply imported into this document.
"""
from api.serializers.Appointments import AppointmentSerializer
from api.serializers.CalendarEvents import CalendarEventSerializer
from api.serializers.Customer import CustomerSerializer
from api.serializers.Menus import GlobalMenuSerializer, StylistMenuSerializer
from api.serializers.PortfolioHaircuts import PortfolioHaircutSerializer
from api.serializers.Shift import ShiftSerializer, ShiftException
from api.serializers.Stylist import StylistSerializer, UnNestedStylistSerializer
from api.serializers.User import UserSerializer
