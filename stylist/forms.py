from django.forms import ModelForm

from core.models import GlobalMenu
from stylist.models import PortfolioHaircut, StylistMenu


class NewPortfolioHaircutForm(ModelForm):
    class Meta:
        model = PortfolioHaircut
        fields = ('name', 'description', 'price')


class MenuOptionForm(ModelForm):
    class Meta:
        model = StylistMenu
        fields = ('name', 'price')