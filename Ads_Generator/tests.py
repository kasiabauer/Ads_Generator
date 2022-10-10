import pytest
from django.contrib.auth.models import User
from django.urls import reverse

from Ads_Generator.models import Campaign


# 1st test checking the system
@pytest.mark.django_db
def test_001_check_settings():
    assert True


# 1st test for index
def test_002_index_view(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200


# 1st test for add campaign
def test_003_add_campaign(client):
    url = reverse('add_campaign')
    response = client.get(url)
    assert response.status_code == 200


# 1st test for campaign list view
@pytest.mark.django_db
def test_004_campaign_list_view(client, campaigns):
    url = reverse('campaigns')
    response = client.get(url)
    campaign = campaigns[0]
    Campaign.objects.remove(campaign)
    assert Campaign.objects.get(campaign.id) == True
    assert response.status_code == 200
    assert response.context['object_list'].count() == len(campaigns)
    for camp in campaigns:
        assert camp in response.context['object_list']


# 1st test for add campaign view
@pytest.mark.django_db
def test_005_add_campaign_post_logged_user(client, users):
    url = reverse('add_campaign')
    redirect_after_post = reverse('campaigns')
    user = users[0]
    client.force_login(user)

    campaign_data = {
        'campaign_name': 'test campaign',
        'user': user
    }
    response = client.post(url, campaign_data)
    assert response.status_code == 302
    assert response.url == redirect_after_post
    Campaign.objects.get(**campaign_data)

