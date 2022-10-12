import pytest
from django.contrib.auth.models import User
from django.urls import reverse

from Ads_Generator.models import Campaign, AdGroup, Keyword


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
    assert response.status_code == 200
    assert response.context['object_list'].count() == len(campaigns)
    for camp in campaigns:
        assert camp in response.context['object_list']


# 1st test for add campaign view
@pytest.mark.django_db
def test_005_add_campaign_post_logged_user(client, users):
    url = reverse('add_campaign')
    user = users[0]
    client.force_login(user)

    campaign_data = {
        'campaign_name': 'test campaign',
        'user': user
    }
    response = client.post(url, campaign_data)
    assert response.status_code == 302
    assert response.url == reverse('campaigns')
    Campaign.objects.get(**campaign_data)


# 1st test for add adgroup view
@pytest.mark.django_db
def test_006_add_adgroup_post_logged_user(client, campaigns, users):
    url = reverse('add_adgroup')
    user = users[0]
    client.force_login(user)
    campaign = campaigns[0]
    adgroup_data = {
        'adgroup_name': 'adgroup1',
        'campaign': campaign.id,
    }
    response = client.post(url, adgroup_data)
    assert response.status_code == 302
    assert response.url == reverse('campaigns')
    AdGroup.objects.get(**adgroup_data)


# 1st test for add adgroup view
@pytest.mark.django_db
def test_007_add_keyword_post_logged_user(client, adgroups, users):
    url = reverse('add_keyword')
    user = users[0]
    client.force_login(user)
    adgroup = adgroups[0]
    keyword_data = {
        'keyword': 'keyword1',
        'adgroup': adgroup.id,
    }
    response = client.post(url, keyword_data)
    assert response.status_code == 302
    assert response.url == reverse('campaigns')
    Keyword.objects.get(**keyword_data)

