from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, UpdateView

from Ads_Generator.forms import UserCreateForm, UserLoginForm, CampaignModelForm, AdgroupModelForm, KeywordModelForm, \
    AdTextTemplateForm, AdTextForm, AdgroupModelFormUpdate, KeywordModelFormUpdate, AdTextTemplateUpdateForm, \
    AdTextUpdateForm
from Ads_Generator.models import Campaign, AdGroup, Keyword, AdText, AdTextTemplate


class IndexView(View):

    def get(self, request):
        return render(request, 'base.html')


class CampaignsListView(ListView):
    model = Campaign
    template_name = 'list_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['headline'] = 'Campaigns'
        context['button'] = 'Add Campaign'
        context['urls'] = 'campaign'
        adtext_template_context = AdTextTemplate.objects.all
        context['adtextstemplate'] = adtext_template_context
        return context


class AdgroupsListView(ListView):
    model = AdGroup
    template_name = 'list_view.html'

    def get_queryset(self):
        new_context = AdGroup.objects.filter(campaign_id=self.request.resolver_match.kwargs['id'])
        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['headline'] = 'Adgroups '
        context['button'] = 'Add Adgroup'
        context['urls'] = 'adgroup'
        return context


class KeywordsAdTextsListView(ListView):
    model = Keyword
    template_name = 'keywords_adtexts_list_view.html'

    def get_queryset(self):
        new_context = Keyword.objects.filter(adgroup_id=self.request.resolver_match.kwargs['id'])
        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        adtext_context = AdText.objects.filter(adgroup_id=self.request.resolver_match.kwargs['id'])
        context['headline'] = 'Keywords & AdTexts'
        context['button'] = 'Add Keyword'
        context['urls'] = 'keyword'
        context['adtexts'] = adtext_context
        return context


class CreateCampaignView(View):

    def get(self, request):
        form = CampaignModelForm()
        return render(request, 'form_item.html', {'form': form, 'headline': 'Add Campaign'})

    def post(self, request):
        form = CampaignModelForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('campaigns')
        return render(request, 'form_item.html', {'form': form, 'headline': 'Add Campaign'})


class UpdateCampaignView(UpdateView):
    model = Campaign
    form_class = CampaignModelForm
    template_name = 'form_rename.html'
    success_url = reverse_lazy('campaigns')


class CreateAdgroupView(View):

    def get(self, request):
        form = AdgroupModelForm
        return render(request, 'form_item.html', {'form': form, 'headline': 'Add AdGroup'})

    def post(self, request):
        form = AdgroupModelForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect('campaigns')
        return render(request, 'form_item.html', {'form': form, 'headline': 'Add AdGroup'})


class UpdateAdgroupView(UpdateView):
    model = AdGroup
    form_class = AdgroupModelFormUpdate
    template_name = 'form_rename.html'
    success_url = reverse_lazy('campaigns')

    # def get_success_url(self):
    #     campaign = AdGroup.objects.get(pk=self._id)
    #     success_url = reverse_lazy('adgroup_list', args=campaign.id)
    #     return success_url


class CreateKeywordView(View):

    def get(self, request):
        form = KeywordModelForm
        return render(request, 'form_item.html', {'form': form, 'headline': 'Add Keyword'})

    def post(self, request):
        form = KeywordModelForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect('campaigns')
        return render(request, 'form_item.html', {'form': form, 'headline': 'Add Keyword'})


class UpdateKeywordView(UpdateView):
    model = Keyword
    form_class = KeywordModelFormUpdate
    template_name = 'form_update.html'
    success_url = reverse_lazy('campaigns')


class CreateAdTextTemplateView(View):

    def get(self, request):
        form = AdTextTemplateForm
        return render(request, 'form_item.html', {'form': form, 'headline': 'Add AdText Template'})

    def post(self, request):
        form = AdTextTemplateForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect('campaigns')
        return render(request, 'form_item.html', {'form': form, 'headline': 'Add AdText Template'})


class UpdateAdTextTemplateView(UpdateView):
    model = AdTextTemplate
    form_class = AdTextTemplateUpdateForm
    template_name = 'form_update.html'
    success_url = reverse_lazy('campaigns')


class CreateAdTextView(View):

    def get(self, request):
        form = AdTextForm
        return render(request, 'form_item.html', {'form': form, 'headline': 'Add AdText'})

    def post(self, request):
        form = AdTextForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect('campaigns')
        return render(request, 'form_item.html', {'form': form, 'headline': 'Add AdText'})


class UpdateAdTextView(UpdateView):
    model = AdText
    form_class = AdTextUpdateForm
    template_name = 'form_update.html'
    success_url = reverse_lazy('campaigns')


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

