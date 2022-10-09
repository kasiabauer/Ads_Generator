import pytest
from django.urls import reverse


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
