from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from rest_framework import viewsets
from .models import Debt
from .serializers import DebtSerializer
from accounts.models import User
from .forms import CreateDebtForm


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


def new_debtor(request):
    if request.method == 'POST':
        user_form = CreateDebtForm(request.POST)
        if user_form.is_valid():
            new_customer = user_form.save(commit=False)
            new_customer.save()
            return render(request, 'new_customer.html', {'new_customer': new_customer})
    else:
        user_form = CreateDebtForm()
    return render(request, 'new_customer.html', {'user_form': user_form})
