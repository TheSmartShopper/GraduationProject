from django.contrib.auth import authenticate, login
from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from accounts.forms import SignupForm
from accounts.models import StoreAdminProfile, CustomerProfile



def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            if form.cleaned_data['typee'] == 'Customer':
                user = authenticate(username=username, password=password)
                CustomerProfile.objects.create(user=user)
                return redirect('accounts:Profile')
            elif form.cleaned_data['typee'] == 'StoreAdmin':
                user = authenticate(username=username, password=password)
                StoreAdminProfile.objects.create(user=user)
                login(request, user)
                return redirect('accounts:Profile')

            else:
                raise Http404("Poll does not exist")
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})


def Profile(request):
    return render(request, 'registration/ProfileView.html', {})
