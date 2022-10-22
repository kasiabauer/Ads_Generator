from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms

from Ads_Generator.models import Campaign, AdGroup, Keyword, AdTextTemplate, AdText


AdTextTemplate_widgets = {
            'campaign': forms.CheckboxSelectMultiple(attrs={'class': 'm-2'}),
            'adtext_template_headline_1': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'adtext_template_headline_2': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'adtext_template_description_1': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'adtext_template_description_2': forms.TextInput(attrs={'class': 'form-control mb-3'}),
        }


AdText_widgets = {
            'adgroup': forms.Select(attrs={'class': 'form-control mt-2'}),
            'adtext_headline_1': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'adtext_headline_2': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'adtext_description_1': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'adtext_description_2': forms.TextInput(attrs={'class': 'form-control mb-3'}),
        }


class UserCreateForm(forms.ModelForm):
    username = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Username')
    password1 = forms.CharField(max_length=128, widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Password')
    password2 = forms.CharField(max_length=128, widget=forms.PasswordInput(attrs={'class': 'form-control mb-3'}), label='Repeat Password')

    class Meta:
        model = User
        fields = ['username']

    def clean(self):
        data = super().clean()
        if data['password1'] != data['password2']:
            raise ValidationError('Passwords are not the same.')

        return data


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-3'}))


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
        exclude = ['adgroup']


class KeywordModelFormUpdate(forms.ModelForm):
    class Meta:
        model = Keyword
        exclude = ['adgroup']


class AdTextTemplateForm(forms.ModelForm):

    class Meta:
        model = AdTextTemplate
        fields = '__all__'
        widgets = AdTextTemplate_widgets
        labels = {
            'campaign': 'Select Campaign/(s)',
        }


class AdTextTemplateUpdateForm(forms.ModelForm):

    class Meta:
        model = AdTextTemplate
        exclude = ['campaign']
        widgets = AdTextTemplate_widgets


class AdTextForm(forms.ModelForm):

    class Meta:
        model = AdText
        fields = '__all__'
        widgets = AdText_widgets
        labels = {
            'adgroup': 'Select Adgroup',
        }


class AdTextUpdateForm(forms.ModelForm):

    class Meta:
        model = AdText
        exclude = ['adgroup']
        widgets = AdText_widgets
