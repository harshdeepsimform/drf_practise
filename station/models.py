from django.db import models
from users.models import CustomUser
# from geopy.geocoders import Nominatim


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class Address(models.Model):
    address = models.CharField(max_length=255, verbose_name='Address')
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default='India')
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)

    class Meta:
        abstract = True


class Station(BaseModel, Address):
    name = models.CharField(max_length=100, verbose_name='Station Name')


class Slot(models.Model):

    SLOT_STATUS = (
        ('A', 'Available'),
        ('O', 'Occupied')
    )

    name = models.CharField(max_length=50, verbose_name='Slot Number')
    station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='slots')
    status = models.CharField(max_length=10, choices=SLOT_STATUS, default='A')


class Schedule(BaseModel):
    '''
    Schedule booking for electric slot    
    '''

    READY = 0
    PROGRESS = 1
    DONE = 2
    CANCEL = 3
    DELAY = 4

    STATUS = (
        (READY, 'Ready'),
        (PROGRESS, 'Progress'),
        (DONE, 'Done'),
        (CANCEL, 'Cancel'),
        (DELAY, 'Delay')
    )

    start_at = models.DateTimeField(null=True)
    end_at = models.DateTimeField(null=True)
    duration = models.IntegerField(verbose_name='Occupied Duration in hrs.')
    status = models.IntegerField(choices=STATUS, default=0)
    customer = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, related_name='schedule', null=True)
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE, related_name='schedule_for')

    def __str__(self):
        return '{} - Station: {} - start_at: {}'.format(self.customer.first_name, self.slot, self.start_at) 

    class Meta:
        indexes = [
            models.Index(fields=['start_at', 'end_at']), #check with customer and slot
            models.Index(fields=['status'], name='status_idx'),
        ]
