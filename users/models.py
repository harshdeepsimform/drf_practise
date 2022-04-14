from distutils.command.upload import upload
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class CustomerManager(models.Manager): #https://docs.djangoproject.com/en/4.0/topics/db/managers/
    def with_counts(self):
        return 1
        # return self.annotate(
        #     num_responses=Coalesce(models.Count("response"), 0)
        # )


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    customer = CustomerManager()

    def __str__(self):
        return self.email


from station.models import Address

class Profile(Address):

    CUSTOMER = 'C'
    STAFF = 'S'

    USER_TYPE = (
        (CUSTOMER, 'Customer'),
        (STAFF, 'Staff')
    )

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='customer/', null=True) #height_field=100, width_field=100
    user_type = models.CharField(max_length=10, choices=USER_TYPE, default='C')

    def __str__(self):
        return self.user.email


class IPRecord(models.Model):
    pub_date = models.DateTimeField('date published')
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return '{} - {}'.format(self.ip_address, self.pub_date)
