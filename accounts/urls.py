"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),

    path('password_change/',
         auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html'),
         name='password_change'),
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
         name='password_change_done'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'),
         name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),
    # Customer view

    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/edit', views.EditProfileView, name='edit_profile'),
    path('signup/', views.signup, name='signup'),
    path('shopping_list', views.shoppinglist, name='Shopping list'),

]
'''


    path('shopping_list', views.shoppinglist, name='Shopping list'),
    path('favorite', views.favorite, name='Favorite'),
    path('Offer', views.Offer, name='Offer'),
    path('reward', views.Reward, name='Reward'),
    path('ProvideReview', views.ProvideReview, name='Provide Review'),


    # Store Admin view
    path('ManageOffer', views.ManageOffer, name='Manage Offer'),
    path('ManagerProduct', views.ManagerProduct, name='Manager Product'),

#System Admin view
    path('ManageAdvertisement', views.ManageAdvertisement, name='Manage Advertisement'),
    path('Manage Reward', views.ManageReward, name='Manage Reward'),
    path('Manage Accounts', views.ManageAccounts, name='Manage Accounts'),


'''