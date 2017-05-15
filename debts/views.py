from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from rest_framework import viewsets
from .models import Debt
from .serializers import DebtSerializer
from accounts.models import User


def customer_list(request):
    customers = Debt.objects.all()
    json = serializers.serialize('json', customers, use_natural_foreign_keys=True, use_natural_primary_keys=True)
    return HttpResponse(json, content_type='application/json')


class DebtViewSet(viewsets.ModelViewSet):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer


def home(request):
    if request.user.is_authenticated:
        templatename = 'home.html'
    else:
        templatename = 'landing.html'
    return render(request, templatename, {})


def reports(request):
    users = User.objects.filter(role='RoleA')
    if request.user in users:
        templatename = 'reports.html'
    else:
        templatename = 'reportforB.html'
    return render(request, templatename, {})
