from django.db.models import Q
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.core import serializers
from django.views.generic import View
from debts.models import Debt
from .forms import SearchForm
from .models import Customer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


# The home view that renders either the landing page or the homepage depending on whether the user is logged in or not
def home(request):
            # Prepare the landing page for rendering
    return render(request, 'landing.html', {})


# view to display list of all the Debts
def customer_list(request):
    debts = Debt.objects.all()
    #  Serializing the data from the queryset to JSON for consumption by the DataTable
    json = serializers.serialize('json', debts, use_natural_foreign_keys=True, use_natural_primary_keys=True,     # This tweak is for converting the customer pk to respective first_name
                                 fields=('customer', 'status', 'amount', 'transaction_time'))                     # and last_name. "fields" restricts the fields to be serialized & displayed
    return HttpResponse(json, content_type='application/json')


@method_decorator(cache_page(60 * 15), name='dispatch')
class Search(View):
    """Search all customers"""
    def get(self, request):
        form = SearchForm()
        params = dict()
        params["form"] = form
        return render(request, 'customers.html', params)

    def post(self, request):
        form = SearchForm(request.POST or None)
        if form.is_valid():
            query = form.cleaned_data['query']
            customers = Customer.objects.filter(Q(idNumber__exact=query) |
                                                Q(phone__exact=query))
            debts = Debt.objects.filter(customer=customers)
            # context = Context({'customers': customers, 'query': query})
            return_str = render_to_string('partials/_customer_search.html',
                                          {'customers': customers, 'query': query, 'debts': debts})
            return JsonResponse(return_str, safe=False)
        else:
            HttpResponseRedirect("/search")


class CustomerAutoComplete(View):
    """Search a hashTag with auto complete feature"""
    def get(self, request):
        query = request.GET['query']
        if query is not None and query is not "":
            customerlist = []
            customers = Customer.objects.filter(idNumber__icontains=query)
            for customer in customers:
                temp = dict()
                temp["query"] = (customer.idNumber)
                customerlist.append(temp)
            return JsonResponse(customerlist, safe=False)
# Profiles views.py