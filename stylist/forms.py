from django.forms import ModelForm

from stylist.models import PortfolioHaircut


class NewPortfolioHaircutForm(ModelForm):
    class Meta:
        model = PortfolioHaircut
        fields = ('name', 'description', 'price')