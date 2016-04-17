from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date

# Create your models here.

class AdminHairDressing(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    street = models.CharField(max_length=200)
    number = models.IntegerField(null=False)
    zipcode = models.CharField(max_length=6)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    description = models.TextField(help_text='Describe la información necesaria de la peluquería')
    url = models.URLField(blank=True, null=True)
    publish_date = models.DateField(auto_now=True)

    def get_absolute_url(self):
        return reverse('hairdressing_detail', kwargs={'pk': self.pk})


    def __str__(self):
        return self.name

class Hairdresser(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    speciality = models.TextField(max_length=100, help_text= 'Redacta las especialidades del peluquero')
    hairdressing = models.ForeignKey(AdminHairDressing, related_name='hairdressers')

    def __str__(self):
        return self.name


class Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    DAY_CHOICES = ((1, 'Lunes'), (2, 'Martes'), (3, 'Miercoles'), (4, 'Jueves'), (5, 'Viernes'), (6, 'Sabado'))
    day = models.PositiveSmallIntegerField('Día', blank=False, default=1, choices=DAY_CHOICES)
    HOUR_CHOICES = ((9, '09:00h'),(10, '10:00h'),(11, '11:00h'),(12, '12:00h'),(13, '13:00h'),(14, '14:00h'),(15, '15:00h'),
                    (16, '16:00h'),(17, '17:00h'),(18, '18:00h'),(19, '19:00h'),(20, '20:00h'),)
    hour = models.PositiveSmallIntegerField('Hora', blank=False, default=1, choices=HOUR_CHOICES)
    hairdresser = models.ForeignKey(Hairdresser, related_name='schedule')

    def __str__(self):
        return self.hairdresser.name + ' - ' + self.get_day_display() + ' - ' + self.get_hour_display()

class Citation(models.Model):
    id = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, related_name='citation')
    id_schedule = models.ForeignKey(Schedule, related_name='citation')

    def __str__(self):
        return 'Cita ' + str(self.id)
