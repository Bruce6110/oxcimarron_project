from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.db.models import Max
from datetime import datetime
from datetime import date

#from oxcimarron.utils import Utils

# Create your models here.


class Resort(models.Model):
    resort_name = models.CharField(max_length=60, null=False, blank=False)
    location = models.CharField(max_length=60)
    skiable_acres = models.IntegerField(default=0)
    base_elevation = models.IntegerField(default=0)
    vertical_feet = models.IntegerField(default=0)
    longest_run = models.DecimalField(
        max_digits=2, decimal_places=1, default=0)
    personal_rating = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return "%s, %s" % (self.resort_name, self.location)

    class Meta:
        ordering = ['resort_name', 'location']


def complex_lookup_on_max_skidate():
    # Find the maximum value of the rating, and then get the record with that rating. Notice the double underscores in rating__max
    print("Max date", max_skidate)
    print("current_date", datetime.now())
    #print("diff: ",datetime.now()-max_skidate)
    delta = datetime.now().date()-max_skidate
    print("DELTA DAYS:",delta.days)

    return SkiDay.objects.get(skidate=max_skidate)


def get_trip_no_default():
    max_skidate = SkiDay.objects.all().aggregate(
        Max('skidate'))['skidate__max']
    last_skiday = SkiDay.objects.get(skidate=max_skidate)
    default_trip_no=last_skiday.trip_no
    delta = datetime.now().date()-max_skidate
    if(delta.days>14):
        default_trip_no+=1
    
    return default_trip_no


class SkiDay(models.Model):
    resort = models.ForeignKey(Resort,
                               on_delete=models.SET_NULL,
                               blank=True,
                               null=True,
                               related_name='skidays',)

    #trip_no = models.IntegerField(blank=True, null=True)
    trip_no = models.IntegerField(
        blank=True, null=True, default=get_trip_no_default)
    skidate = models.DateField(verbose_name="Date", default=timezone.now)
    #resort = models.ForeignKey(Resort, null=True, on_delete=models.SET_NULL)

    miles = models.DecimalField(
        blank=True, null=True, max_digits=3, decimal_places=1)
    miles_alt = models.DecimalField(
        blank=True, null=True, max_digits=3, decimal_places=1)

    top_speed = models.DecimalField(
        blank=True, null=True, max_digits=3, decimal_places=1)
    top_speed_alt = models.DecimalField(
        blank=True, null=True, max_digits=3, decimal_places=1)

    vertical_feet = models.IntegerField(blank=True, null=True)
    vertical_feet_alt = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.skidate) + " - " + str(self.resort)

    def get_absolute_url(self):
        return reverse('skiday-update', args=[str(self.id)])

    class Meta:
        ordering = ['-skidate']
