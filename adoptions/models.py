from django.db import models as m


class Pet(m.Model):
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
    name = m.CharField(max_length=100)
    age = m.IntegerField(null='True')
    submitter = m.CharField(max_length=100)
    species = m.CharField(max_length=50, blank='True')
    breed = m.CharField(max_length=50, blank='True')
    color = m.CharField(max_length=20)
    description = m.TextField()
    sex = m.CharField(max_length=1, choices=SEX_CHOICES, blank='True')
    submission_date = m.DateTimeField(blank='True')
    vaccinations = m.ManyToManyField('Vaccine', blank='True')


class Vaccine(m.Model):
    name = m.CharField(max_length=50, blank='True')

    def __str__(self):
        return self.name
