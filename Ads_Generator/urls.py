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
    path("campaign/<int:id>/", views.AdgroupsListView.as_view(), name='adgroup_list'),
    path("adgroup/<int:id>/", views.KeywordsAdTextsListView.as_view(), name='keyword_list'),
    path("campaigns/add_campaign/", views.CreateCampaignView.as_view(), name='add_campaign'),
    path("campaign/<int:campaign_id>/add_adgroup/", views.CreateAdgroupView.as_view(), name='add_adgroup'),
    path("adgroup/<int:adgroup_id>/add_keyword/", views.CreateKeywordView.as_view(), name='add_keyword'),
    path("add_adtext_template/", views.CreateAdTextTemplateView.as_view(), name='add_adtext_template'),
    path("add_adtext/", views.CreateAdTextView.as_view(), name='add_adtext'),
    path('update_campaign/<int:pk>/', views.UpdateCampaignView.as_view(), name='update_campaign'),
    path('update_adgroup/<int:pk>/', views.UpdateAdgroupView.as_view(), name='update_adgroup'),
    path('adgroup/<int:adgroup_id>/update_keyword/<int:pk>/', views.UpdateKeywordView.as_view(), name='update_keyword'),
    path('update_adtext_template/<int:pk>/', views.UpdateAdTextTemplateView.as_view(), name='update_adtext_template'),
    path('adgroup/<int:adgroup_id>/update_adtext/<int:pk>/', views.UpdateAdTextView.as_view(), name='update_adtext'),
    path('delete_campaign/<int:pk>/', views.CampaignDelete.as_view(), name='delete_campaign'),
    path('campaign/<int:campaign_id>/delete_adgroup/<int:pk>/', views.AdgroupDeleteView.as_view(), name='delete_adgroup'),
    path("adgroup/<int:adgroup_id>/delete_keyword/<int:pk>/", views.KeywordDeleteView.as_view(), name='delete_keyword'),
    path("adgroup/<int:adgroup_id>/delete_adtext/<int:pk>/", views.AdTextDeleteView.as_view(), name='delete_adtext'),
    path("adgroup/<int:adgroup_id>/generate_adtext/", views.GenerateAdText.as_view(), name='generate_adtext'),
    path("delete_adtext_template/<int:pk>/", views.AdTextTemplateDeleteView.as_view(), name='delete_template'),

]
