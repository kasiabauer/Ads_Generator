from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from Ads_Generator.forms import UserCreateForm, UserLoginForm


class IndexView(View):
    def get(self, request):
        return render(request, 'base.html')


class CampaignsView(View):
    def get(self, request):
        return render(request, 'campaigns.html')


class RegisterUser(View):

    def get(self, request):
        form = UserCreateForm()
        return render(request, 'form.html', {'form': form, 'headline': 'Register'})

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


class LoginUser(View):

    def get(self, request):
        form = UserLoginForm()
        return render(request, 'form.html', {'form': form, 'headline': 'Login'})

    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                url = request.GET.get('next', '/')
                login(request, user)
        return redirect(url)


class LogoutUser(View):

    def get(self, request):

        username = request.user.username
        logout(request)
        return render(request, 'base.html', {'msg': f'{username} was logged out'})

