from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms

from Ads_Generator.models import Campaign, AdGroup, Keyword, AdTextTemplate, AdText


class UserCreateForm(forms.ModelForm):
    password1 = forms.CharField(max_length=128, widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(max_length=128, widget=forms.PasswordInput, label='Repeat Password')

    class Meta:
        model = User
        fields = ['username']


    def clean(self):
        data = super().clean()
        if data['password1'] != data['password2']:
            raise ValidationError('Passwords are not the same.')

        return data


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=128)
    password = forms.CharField(widget=forms.PasswordInput)


class CampaignModelForm(forms.ModelForm):
    class Meta:
        model = Campaign
        exclude = ['user']


class AdgroupModelForm(forms.ModelForm):
    class Meta:
        model = AdGroup
        fields = ['adgroup_name']


class AdgroupModelFormUpdate(forms.ModelForm):
    class Meta:
        model = AdGroup
        exclude = ['campaign']


class KeywordModelForm(forms.ModelForm):
    class Meta:
        model = Keyword
        fields = '__all__'


class KeywordModelFormUpdate(forms.ModelForm):
    class Meta:
        model = Keyword
        exclude = ['adgroup']


class AdTextTemplateForm(forms.ModelForm):

    class Meta:
        model = AdTextTemplate
        fields = '__all__'


class AdTextTemplateUpdateForm(forms.ModelForm):

    class Meta:
        model = AdTextTemplate
        exclude = ['campaign']


class AdTextForm(forms.ModelForm):

    class Meta:
        model = AdText
        fields = '__all__'


class AdTextUpdateForm(forms.ModelForm):

    class Meta:
        model = AdText
        exclude = ['adgroup']
