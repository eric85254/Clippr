from django.db import models


#todo: use this model.
class Deal(models.Model):
    """
        This is a model created to hold the deals that a stylist offers.
        It's not really in use yet.
    """
    stylist = models.ForeignKey('core.User', on_delete=models.CASCADE)
    description = models.TextField()
    price_modifier = models.DecimalField


class PortfolioHaircut(models.Model):
    """
        Model to hold portfolio haircuts.
            **fields:**
                :param stylist: foreign key to User database
                :param picture: FileField
                :param name: Character Field
                :param description: Text Field (Text field has no max character length)
                :param price: Decimal Field
                :param menu_option: foreign key to StylistMenu
    """
    stylist = models.ForeignKey('core.User', on_delete=models.CASCADE, null=True, blank=True)
    picture = models.FileField(upload_to='haircuts/%Y/%m/%d', null=True, blank=True)
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    menu_option = models.ForeignKey('core.StylistMenu', null=True, blank=True)

    def __str__(self):
        return self.stylist.username + ' || ' + self.name
