from django.db import models

class FullCalendarEvent(models.Model):
    title = models.TextField(blank=True)
    allDay = models.NullBooleanField(default=False, null=True, blank=True)
    start = models.TextField(blank=True)
    end = models.TextField(blank=True)
    url = models.URLField(null=True, blank=True)
    editable = models.NullBooleanField(null=True, blank=True)
    startEditable = models.NullBooleanField(null=True, blank=True)
    durationEditable = models.NullBooleanField(null=True, blank=True)
    resourceEditable = models.NullBooleanField(null=True, blank=True)
    rendering = models.TextField(blank=True)
    overlap = models.NullBooleanField(null=True, blank=True)

    color = models.TextField(null=True, blank=True)
    backgroundColor = models.TextField(null=True, blank=True)
    borderColor = models.TextField(null=True, blank=True)
    textColor = models.TextField(null=True, blank=True)
    #constraint = models.ForeignKey('core.EventID')...
    #source = models.ForeignKey('core.EventSourceObject')

    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 0
    dow = models.CharField(max_length=17, blank=True, null=True)

    start_date_time = models.DateTimeField(null=True, blank=True)
    end_date_time = models.DateTimeField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        if self.start_date_time is None or self.start_date_time == '':
            self.start = str(self.start_time)
        else:
            self.start = str(self.start_date_time)

        if self.end_date_time is None or self.end_date_time == '':
            self.end = str(self.end_time)
        else:
            self.end = str(self.end_date_time)

        super(FullCalendarEvent, self).save()