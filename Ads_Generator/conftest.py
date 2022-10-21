import pytest
from django.contrib.auth.models import User

from Ads_Generator.models import Campaign, AdGroup, Keyword, AdText, AdTextTemplate


@pytest.fixture
def users():
    lst = []
    for x in range(10):
        lst.append(User.objects.create(username=str(x)))
    return lst


@pytest.fixture
def user():
    return User.objects.create(username='test user')


@pytest.fixture
def campaigns(users):
    lst = []
    for user in users:
        lst.append(Campaign.objects.create(campaign_name='test_campaign', user=user))
    return lst


@pytest.fixture
def adgroups(campaigns):
    lst = []
    for campaign in campaigns:
        lst.append(AdGroup.objects.create(adgroup_name='test_adgroup', campaign=campaign))
    return lst


@pytest.fixture
def keywords(adgroups):
    lst = []
    for adgroup in adgroups:
        lst.append(Keyword.objects.create(keyword='test_keyword', adgroup=adgroup))
    return lst


@pytest.fixture
def adtexts(adgroups):
    lst = []
    for adgroup in adgroups:
        lst.append(AdText.objects.create(
            adtext_headline_1='test headline1',
            adtext_headline_2='test headline2',
            adtext_description_1='test description 1',
            adtext_description_2='test description 2',
            adgroup=adgroup))
    return lst


@pytest.fixture
def adtext_templates(campaigns):
    lst = []
    for campaign in campaigns:
        x = AdTextTemplate.objects.create(
            adtext_template_headline_1='test template headline1',
            adtext_template_headline_2='test template headline2',
            adtext_template_description_1='test template description 1',
            adtext_template_description_2='test template description 2',
            )
        x.campaign.add(campaign)
        lst.append(x)
    return lst
