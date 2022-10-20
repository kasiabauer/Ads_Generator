from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Campaign(models.Model):
    campaign_name = models.CharField(max_length=128)  # UNIQUE_TOGETHER (poprzez klasę Meta)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.campaign_name}'


class AdGroup(models.Model):
    adgroup_name = models.CharField(max_length=128)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.adgroup_name}'


class Keyword(models.Model):
    keyword = models.CharField(max_length=64)
    adgroup = models.ForeignKey(AdGroup, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.keyword}'


class AdText(models.Model):
    adtext_headline_1 = models.CharField(max_length=64)
    adtext_headline_2 = models.CharField(max_length=64)
    adtext_description_1 = models.CharField(max_length=128)
    adtext_description_2 = models.CharField(max_length=128)
    adgroup = models.ForeignKey(AdGroup, on_delete=models.CASCADE)

    def __str__(self):
        return f'AdText with headline1: {self.adtext_headline_1}'


class AdTextTemplate(models.Model):
    adtext_template_headline_1 = models.CharField(max_length=64)
    adtext_template_headline_2 = models.CharField(max_length=64)
    adtext_template_description_1 = models.CharField(max_length=128)
    adtext_template_description_2 = models.CharField(max_length=128)
    campaign = models.ManyToManyField(Campaign, blank=True)

    def __str__(self):
        return f'Template: {self.pk}'

