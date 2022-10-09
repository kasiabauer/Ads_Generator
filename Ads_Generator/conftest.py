import pytest
from django.contrib.auth.models import User

from Ads_Generator.models import Campaign


@pytest.fixture
def campaigns(users):
    lst = []
    for user in users:
        lst.append(Campaign.objects.create(campaign_name='test_campaign', user=user))
    return lst


@pytest.fixture
def users():
    lst = []
    for x in range(10):
        lst.append(User.objects.create(username=x))
        return lst
