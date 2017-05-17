from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UserRegistrationForm
from .models import User

# Create your views here.


# def register(request):
#     if request.method == 'POST':
#         user_form = UserRegistrationForm(request.POST)
#         if user_form.is_valid():
#             new_user = user_form.save(commit=False)
#             new_user.set_password(user_form.cleaned_data['password'])
#             new_user.save()
#             return render(request, 'register_done.html', {'new_user': new_user})
#     else:
#         user_form = UserRegistrationForm()
#     return render(request, 'register.html', {'user_form': user_form})


def new_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                            user_password=form.cleaned_data['user_password'],
                                            user_role=form.cleaned_data['user_role'])
            user.save()
            return render(request, 'home.html', {})
    else:
        form = UserRegistrationForm()
    return render(request, 'new.html', {'form': form})
