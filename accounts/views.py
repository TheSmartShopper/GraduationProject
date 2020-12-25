from audioop import reverse

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404,HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View

import accounts
from accounts.forms import SignupForm, CustomerProfileForm, StoreAdminProfileForm, UserForm
from accounts.models import StoreAdminProfile, CustomerProfile


# Create your views here.


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


def get_user(request):
    try:
        return type(CustomerProfile.objects.get(user=request.user))
    except CustomerProfile.DoesNotExist:
        try:
            return type(StoreAdminProfile.objects.get(user=request.user))
        except StoreAdminProfile.DoesNotExist:
            pass


class ProfileView(View):
    template_name = 'registration/ProfileView.html'
    userProfile = None
    user = None

    def get(self, request):
        self.user = (UserForm(instance=User.objects.get(pk=request.user.pk)))

        if get_user(request) == accounts.models.CustomerProfile:
            self.Get_CustomerProfile(request)
            return render(request, self.template_name, {'form': self.userProfile, 'user': self.user})

        elif get_user(request) == accounts.models.StoreAdminProfile:
            self.Get_StoreAdminProfile(request)
            return render(request, self.template_name, {'form': self.userProfile, 'user': self.user})
        else:
            raise Http404

    def Get_CustomerProfile(self, request):
        self.userProfile = CustomerProfileForm(instance=(CustomerProfile.objects.get(user=request.user)))

    def Get_StoreAdminProfile(self, request):
        self.userProfile = StoreAdminProfileForm(instance=(StoreAdminProfile.objects.get(user=request.user)))


@login_required
def EditProfileView(request):
    userProfile = None
    userForm = None
    profileForm = None

    if request.method == 'POST':
        userForm = UserForm(request.POST, instance=request.user)
        if get_user(request) == accounts.models.CustomerProfile:
            userProfile = CustomerProfile.objects.get(user=request.user)
            profileForm = CustomerProfileForm(request.POST, request.FILES, instance=userProfile)

        elif get_user(request) == accounts.models.StoreAdminProfile:
            userProfile = StoreAdminProfile.objects.get(user=request.user)
            profileForm = StoreAdminProfileForm(request.POST, request.FILES, instance=userProfile)
        else:
            raise Http404
        if userForm.is_valid() and profileForm.is_valid():
            userForm.save()
            myprofile = profileForm.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect('accounts:profile')

    else:
        userForm = UserForm(instance=request.user)
        if get_user(request) == accounts.models.CustomerProfile:
            userProfile = CustomerProfile.objects.get(user=request.user)
            profileForm = CustomerProfileForm( instance=userProfile)

        elif get_user(request) == accounts.models.StoreAdminProfile:
            userProfile = StoreAdminProfile.objects.get(user=request.user)
            profileForm = StoreAdminProfileForm( instance=userProfile)
        else:
            raise Http404

    return render(request, 'registration/ProfileEditView.html', {'userForm': userForm, 'profileForm': profileForm})




def shoppinglist(request):
    return HttpResponse('ksmvonvjv')