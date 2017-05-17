from django.conf.urls import url
from accounts.auth import views as auth_views
from .views import new_user
from .forms import CustomAuthenticationForm

urlpatterns = [
    url(r'^login/$', auth_views.login, {
        'authentication_form': CustomAuthenticationForm}, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),

    url(r'^new/$', new_user, name='new_user'),
]
