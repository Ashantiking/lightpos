from io import BytesIO
from PIL import Image
from easy_thumbnails.fields import ThumbnailerImageField
from django.core.files import File

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Company(models.Model):
    logo = models.ImageField(upload_to='uploads/', blank=True, null=True)
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=555)
    phone = models.CharField(max_length=500)
    email = models.EmailField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return str(self.name) + ' | ' + (self.address) + ' | ' + str(self.phone) + ' | ' + str(self.email)


class Developer(models.Model):
    photo = ThumbnailerImageField(upload_to='photos', blank=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=500)
    email = models.EmailField()
    about = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return str(self.name) + ' | ' + (self.address) + ' | ' + str(self.phone) + ' | ' + str(self.email)


class Staff(models.Model):
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    staff_name = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=200)
    staff_id = models.CharField(max_length=20)
    phone = models.CharField(max_length=500)
    email = models.EmailField()

    class Meta:
        ordering = ['staff_name']

    def __str__(self):
        return str(self.staff_name) + ' | ' + (self.position) + ' | ' + str(self.phone) + ' | ' + str(self.email)
