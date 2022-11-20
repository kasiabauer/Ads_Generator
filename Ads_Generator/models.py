from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse


class Campaign(models.Model):
    campaign_name = models.CharField(max_length=128)  # UNIQUE_TOGETHER (poprzez klasę Meta)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['campaign_name', 'user'], name="user-campaigns")
        ]

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
    adtext_headline_1 = models.CharField(max_length=30)
    adtext_headline_2 = models.CharField(max_length=30)
    adtext_description_1 = models.CharField(max_length=90)
    adtext_description_2 = models.CharField(max_length=90)
    adgroup = models.ForeignKey(AdGroup, on_delete=models.CASCADE)

    def __str__(self):
        return f'AdText with headline1: {self.adtext_headline_1}'


def keyword_occurrence_in_string(value):
    return value.count('{keyword}')


def headline_with_keyword_validation(value):
    num_of_keywords = keyword_occurrence_in_string(value)
    headline_char_limit = 30 - num_of_keywords
    if '{keyword}' in value:
        num_of_keywords = keyword_occurrence_in_string(value)
        value_without_keyword = value.replace('{keyword}', '')
        chars = len(value_without_keyword)
        if chars > headline_char_limit:
            raise ValidationError(f'Character limit exceeded by: {chars - headline_char_limit - num_of_keywords}. '
                                  f'Overall chars: {chars - num_of_keywords} '
                                  f' ({num_of_keywords} character/(s) reserved for keyword)')


def description_with_keyword_validation(value):
    num_of_keywords = keyword_occurrence_in_string(value)
    description_char_limit = 90 - num_of_keywords
    if '{keyword}' in value:
        value_without_keyword = value.replace('{keyword}', '')
        chars = len(value_without_keyword)
        if chars > description_char_limit:
            raise ValidationError(f'Char limit exceeded '
                                  f'by: {chars - description_char_limit - num_of_keywords}. '
                                  f'Overall chars: {chars - num_of_keywords} '
                                  f'({num_of_keywords} character/(s) reserved for keyword)')


class AdTextTemplate(models.Model):
    adtext_template_headline_1 = models.CharField(max_length=270, validators=[headline_with_keyword_validation])
    adtext_template_headline_2 = models.CharField(max_length=270, validators=[headline_with_keyword_validation])
    adtext_template_description_1 = models.CharField(max_length=810, validators=[description_with_keyword_validation])
    adtext_template_description_2 = models.CharField(max_length=810, validators=[description_with_keyword_validation])
    campaign = models.ManyToManyField(Campaign, blank=True)

    def __str__(self):
        return f'Template: {self.pk}'

