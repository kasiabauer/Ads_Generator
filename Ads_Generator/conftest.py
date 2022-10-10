import pytest
from django.contrib.auth.models import User

from Ads_Generator.models import Campaign, AdGroup


@pytest.fixture
def users():
    lst = []
    for x in range(10):
        lst.append(User.objects.create(username=str(x)))
        return lst


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


