"""
iDebtor URL Configuration

The "urlpatterns" list routes URLs to views, i.e maps the various views to the respective

"""
from django.conf.urls import url, include


urlpatterns = [

    # url(r'^admin/', admin.site.urls),
    # url(r'^', include('django.contrib.auth.urls')),
    url(r'^', include('accounts.urls')),
    url(r'^', include('debts.urls')),


]
