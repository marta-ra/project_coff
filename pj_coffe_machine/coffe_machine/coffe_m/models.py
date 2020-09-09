from django.db import models
from django.db.models import fields
from django.http import HttpResponse, request, HttpResponseRedirect
from django.shortcuts import reverse, render


class Point_address(models.Model):
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    house = models.IntegerField()

    def __str__(self):
        return '{}, {}, {}'.format(self.city, self.street, self.house)


class Point_coffemachine(models.Model):
    client_point = models.CharField(max_length=255, verbose_name='Customer point', null=True)
    client_name = models.CharField(max_length=255, verbose_name='Client name')
    point_address = models.OneToOneField(Point_address, related_name='Pointaddress', on_delete=models.SET_NULL,
                                         null=True)
    manager_name = models.CharField(max_length=255)
    manager_telephone = models.CharField(max_length=255)
    region = models.CharField(max_length=255, verbose_name='Point region')

    # coffemachines = models.ForeignKey(Coffemachine, related_name='Coffemachines', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return '{}, {}'.format(self.client_point, self.client_name)


class Coffemachine(models.Model):
    model = models.CharField(max_length=255, verbose_name='Model')
    point = models.ForeignKey(Point_coffemachine, related_name='Coffemachines', on_delete=models.SET_NULL, null=True)

    # visits = models.ForeignKey(Visit, related_name='Visits', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return '{}, {}'.format(self.model, self.point)


class Visit(models.Model):
    coffemachine = models.ForeignKey(Coffemachine, related_name='visits', on_delete=models.SET_NULL, null=True)
    visit_date = models.DateField(verbose_name='Date of visit')
    technical_specialist = models.CharField(max_length=255, verbose_name='Technical specialist')
    done = models.CharField(max_length=255, verbose_name='What was done during the visit?')
    renovation = models.BooleanField(verbose_name='Was there a renovation')
    what_renovation = models.CharField(max_length=255, verbose_name='What was the repair?')

    def __str__(self):
        return '{}, {}, {}'.format(self.coffemachine, self.visit_date, self.technical_specialist)

    #def get_absolute_url(self):
        #return HttpResponseRedirect('/')

    # return reverse('visit:create_visit', args=[self.id, ])

    # class Meta:
    #     ordering = ('-client_name',)

class Useful_code(models.Model):
    description = models.CharField(max_length=255, verbose_name='Описание кода')
    code = models.CharField(max_length=255, verbose_name='Код')

    def __str__(self):
        return '{}: {}'.format(self.description, self.code)


class Useful_docs(models.Model):
    model_machine = models.CharField(max_length=255, verbose_name='Модель кофемашины')
    document = models.FileField(max_length=255, verbose_name='Документация')

    def __str__(self):
        return '{}: {}'.format(self.model_machine, self.document)