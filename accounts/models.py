import datetime

from django.contrib.auth.models import User
from django.db import models
# Create your models here.
from django.utils.text import slugify
from django_countries.fields import CountryField

Customer_type = (
    ('Customer', 'Customer'),
    ('StoreAdmin', 'StoreAdmin'),
)


class StoreAdminProfile(models.Model):
    Is_StoreAdmin = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    StoreAdmin_slug = models.SlugField(blank=True, null=True)
    StoreAdmin_image = models.ImageField(upload_to='profile_img', blank=True, null=True)
    StoreAdmin_address = models.CharField(max_length=100)
    StoreAdmin_join_date = models.DateTimeField(default=datetime.datetime.now)
    StoreAdmin_country = CountryField(default='Jordan')

    # Create your models here.

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user)
        super(StoreAdminProfile, self).save(*args, **kwargs)

    def UserType(self):
        return 'StoreAdmin'


class CustomerProfile(models.Model):
    Is_Customer = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Customer_slug = models.SlugField(blank=True, null=True)
    Customer_image = models.ImageField(upload_to='profile_img', blank=True, null=True)
    Customer_address = models.CharField(max_length=100)
    Customer_join_date = models.DateTimeField(default=datetime.datetime.now)
    Customer_country = CountryField(default='Jordan')

    # Create your models here.

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user)
        super(CustomerProfile, self).save(*args, **kwargs)

    def UserType(self):
        return 'Customer'
