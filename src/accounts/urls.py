from django.conf.urls import url
from django.contrib.auth import views as auth_views

from .forms import CustomAuthenticationForm

urlpatterns = [
    url(r'^login/$', auth_views.login, {
        'authentication_form': CustomAuthenticationForm}, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
]
