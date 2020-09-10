from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView

from . import models
from django import forms
from django.http import HttpResponseRedirect
from .forms import VisitForm
from .forms import Useful_codeForm
from .forms import Useful_docsForm
from .models import Point_coffemachine
from .models import Visit
from .models import Coffemachine



def all_clients(request):
    points = models.Point_coffemachine.objects.all()
    cods = models.Useful_code.objects.all()
    docs = models.Useful_docs.objects.all()
    return render(request, 'coffe/clients.html', {'points': points, 'cods': cods, 'docs': docs})


def report_visits(request):
    report_visit = Visit.objects.all()
    point = Point_coffemachine.objects.all()
    coffemachine = Coffemachine.objects.all()
    merge = Coffemachine.objects.all()
    return render(request, 'coffe/reports.html', {'report_visit': report_visit, 'point': point, 'coffemachine': coffemachine, 'merge': merge})

def useful_code(request):
    useful_code = models.Useful_code.objects.all()
    return render(request, 'coffe/useful_code.html', {'useful_code': useful_code})

def useful_docs(request):
    useful_docs = models.Useful_docs.objects.all()
    return render(request, 'coffe/useful_docs.html', {'useful_docs': useful_docs})

class Create_visit(CreateView):
    form_class = VisitForm
    template_name = 'coffe/create_visit.html'

class Create_Useful_code(CreateView):
    form_class = Useful_codeForm
    template_name = 'coffe/create_useful_code.html'

class Create_Useful_docs(CreateView):
    form_class = Useful_docsForm
    template_name = 'coffe/create_useful_docs.html'