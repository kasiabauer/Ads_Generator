from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from Ads_Generator.forms import UserCreateForm


class IndexView(View):
    def get(self, request):
        return render(request, 'base.html')


class CampaignsView(View):
    def get(self, request):
        return render(request, 'campaigns.html')


class RegisterUser(View):

    def get(self, request):
        form = UserCreateForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = UserCreateForm(request.POST)
        if form.is_valid():
            un = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            u = User()
            u.username = un
            u.set_password(password)
            u.save()
            return redirect('/')
        return render(request, 'form.html', {'form': form})
