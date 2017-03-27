from django.db import models

# todo: use this model.
from core.utils.abstract_classes import FullCalendarEvent


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
    menu_option = models.ForeignKey('stylist.StylistMenu', null=True, blank=True)
    duration = models.DurationField()

    def __str__(self):
        return self.stylist.username + ' || ' + self.name


class StylistMenu(models.Model):
    """
        A stylist's unique menu option.
        | If the stylist makes a modification to the Global Menu option then their modification is stored here
        as a new Menu option and it is tied to the Global Menu through the field modified_global.
    """
    stylist = models.ForeignKey('core.User', related_name='menu_owner')
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    modified_global = models.ForeignKey('core.GlobalMenu', related_name='modified_global', null=True, blank=True)
    duration = models.DurationField()

    def __str__(self):
        return "Stylist: " + self.stylist.get_full_name() + " || Name: " + self.name


class Shift(FullCalendarEvent):
    """
        Model to hold shift schedule of Stylist
    """
    owner = models.ForeignKey('core.User', related_name='shift_owner')
    is_shift = models.BooleanField(default=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.is_shift = True
        super(Shift, self).save()

    def get_exceptions(self):
        exceptions = ShiftException.objects.filter(shift=self)
        return exceptions


class ShiftException(models.Model):
    shift = models.ForeignKey('stylist.Shift', related_name='shift', on_delete=models.CASCADE)
    start = models.DateField()
    end = models.DateField()
