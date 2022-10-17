"""Ads_Generator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from Ads_Generator import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.IndexView.as_view(), name='index'),
    path("register/", views.RegisterUser.as_view(), name='register'),
    path("login/", views.LoginUser.as_view(), name='login'),
    path("logout/", views.LogoutUser.as_view(), name='logout'),
    path("campaigns/", views.CampaignsListView.as_view(), name='campaigns'),
    path("add_campaign/", views.CreateCampaignView.as_view(), name='add_campaign'),
    path("add_adgroup/", views.CreateAdgroupView.as_view(), name='add_adgroup'),
    path("add_keyword/", views.CreateKeywordView.as_view(), name='add_keyword'),
    path("add_adtext_template/", views.CreateAdTextTemplateView.as_view(), name='add_adtext_template'),
    path("add_adtext/", views.CreateAdTextView.as_view(), name='add_adtext'),
]