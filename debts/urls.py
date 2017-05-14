from django.conf.urls import url, include
from rest_framework import routers
from . import views
from profiles.views import (Search,
                            CustomerAutoComplete
                            )

# Registering the REST API routes
customer_router = routers.DefaultRouter()
customer_router.register(r'customers', views.DebtViewSet, base_name='customers')
urlpatterns = [

    url(r'^api/', include(customer_router.urls)),                   # This is the REST API endpoint URL

    url(r'^$', views.home, name='home'),

    url(r'^reports/$', views.reports, name='reports'),

    url(r'^search/$', Search.as_view(), name='search'),                  # This is the Landing Page/Home View
    url(r'^customer.json$', CustomerAutoComplete.as_view()),

    url(r'^api_json/$', views.customer_list, name='customer_list'),  # this is the URL for the serialized JSON output of Debts
]
