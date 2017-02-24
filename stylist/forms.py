from django.forms import ModelForm

from core.models import Menu
from stylist.models import PortfolioHaircut


class NewPortfolioHaircutForm(ModelForm):
    class Meta:
        model = PortfolioHaircut
        fields = ('name', 'description', 'price')


class MenuOptionForm(ModelForm):
    class Meta:
        model = Menu
        fields = ('name', 'price', 'description')