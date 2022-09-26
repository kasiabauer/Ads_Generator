from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request):
        return render(request, 'base.html')


class CampaignsView(View):
    def get(self, request):
        return render(request, 'campaigns.html')
