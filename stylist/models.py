from django.db import models


# Change price_modifier field name to price
class Deal(models.Model):
    stylist = models.ForeignKey('core.User', on_delete=models.CASCADE)
    description = models.TextField()
    price_modifier = models.DecimalField


class PortfolioHaircut(models.Model):
    stylist = models.ForeignKey('core.User', on_delete=models.CASCADE, null=True, blank=True)
    picture = models.FileField(upload_to='haircuts/%Y/%m/%d', null=True, blank=True)
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    menu_option = models.ForeignKey('core.Menu', null=True, blank=True)

    def __str__(self):
        return self.stylist.username + ' || ' + self.name


class StylistBridgeMenu(models.Model):
    stylist = models.ForeignKey('core.User', on_delete=models.CASCADE)
    menu_option = models.ForeignKey('core.Menu', on_delete=models.CASCADE)

    # This price should override the price of default menu_options - hard to do with template :(
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
