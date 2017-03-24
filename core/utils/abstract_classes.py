from django.db import models

class FullCalendarEvent(models.Model):
    title = models.TextField(blank=True, default="")
    allDay = models.BooleanField(default=False)
    start = models.TextField(blank=True, default="")
    end = models.TextField(blank=True, default="")
    url = models.URLField(blank=True, default="")
    editable = models.BooleanField(default=False)
    startEditable = models.BooleanField(default=True)
    durationEditable = models.BooleanField(default=False)
    resourceEditable = models.BooleanField(default=False)
    rendering = models.TextField(blank=True, default="")
    overlap = models.BooleanField(default=False)

    color = models.TextField(blank=True, default="")
    backgroundColor = models.TextField(blank=True, default="")
    borderColor = models.TextField(blank=True, default="")
    textColor = models.TextField(null=True, blank=True, default="")
    #constraint = models.ForeignKey('core.EventID')...
    #source = models.ForeignKey('core.EventSourceObject')

    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 0
    dow = models.CharField(max_length=17, blank=True, default="")

    start_date_time = models.DateTimeField(blank=True, null=True)
    end_date_time = models.DateTimeField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)

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