import pytest
from django.contrib.auth.models import User
from django.urls import reverse

from Ads_Generator.models import Campaign, AdGroup, Keyword, AdTextTemplate, AdText


# 1st test checking the system
@pytest.mark.django_db
def test_001_check_settings():
    assert True


# 1st test for index
def test_002_index_view(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200


# 2nd test for index view
@pytest.mark.django_db
def test_23_index_view_logged_user(client, users):
    url = reverse('index')
    user = users[0]
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200


# 1st test for add campaign view
def test_003_add_campaign_not_logged_user(client):
    url = reverse('add_campaign')
    response = client.get(url)
    assert response.status_code == 302


# 2nd test for add campaign view
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


# 1st test for campaign list view
@pytest.mark.django_db
def test_004_campaign_list_view(client, campaigns):
    url = reverse('campaigns')
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['object_list'].count() == len(campaigns)
    for camp in campaigns:
        assert camp in response.context['object_list']


# 2nd test for campaign list view
@pytest.mark.django_db
def test_010_campaigns_list_view_logged_user(client, campaigns, users):
    url = reverse('campaigns')
    user = users[0]
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['object_list'].count() == len(campaigns)


# 1st test for add adgroup view
@pytest.mark.django_db
def test_006_add_adgroup_post_logged_user(client, campaigns, users):
    campaign = campaigns[0]
    url = reverse('add_adgroup', args=(campaign.id,))
    user = users[0]
    client.force_login(user)
    adgroup_data = {
        'adgroup_name': 'adgroup1',
        'campaign': campaign.id,
    }
    response = client.post(url, adgroup_data)
    assert response.status_code == 302
    assert response.url == reverse('adgroup_list', args=(campaign.id,))
    AdGroup.objects.get(**adgroup_data)


# 2nd test for add adgroup view
@pytest.mark.django_db
def test_024_add_adgroup_post(client, campaigns, users):
    campaign = campaigns[0]
    url = reverse('add_adgroup', args=(campaign.id,))
    adgroup_data = {
        'adgroup_name': 'adgroup1',
        'campaign': campaign.id,
    }
    response = client.post(url, adgroup_data)
    assert response.status_code == 302
    url_redirect = reverse('login')
    assert response.url.startswith(url_redirect)


# 1st test for add keyword view
@pytest.mark.django_db
def test_007_add_keyword_post_logged_user(client, adgroups, users):
    adgroup = adgroups[0]
    url = reverse('add_keyword', args=(adgroup.id, ))
    user = users[0]
    client.force_login(user)
    keyword_data = {
        'keyword': 'keyword1',
        'adgroup': adgroup.id,
    }
    response = client.post(url, keyword_data)
    assert response.status_code == 302
    assert response.url == reverse('keyword_list', args=(adgroup.id, ))
    Keyword.objects.get(**keyword_data)


# 2nd test for add keyword view
@pytest.mark.django_db
def test_024_add_keyword_get_logged_user(client, adgroups, users):
    adgroup = adgroups[0]
    url = reverse('add_keyword', args=(adgroup.id, ))
    user = users[0]
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200


# 1st test for add template view
@pytest.mark.django_db
def test_008_add_adtext_template_post_logged_user(client, campaigns, users):
    url = reverse('add_adtext_template')
    user = users[0]
    client.force_login(user)
    campaign = campaigns[0]
    adtext_template_data = {
        'adtext_template_headline_1': 'test template headline 1',
        'adtext_template_headline_2': 'test template headline 2',
        'adtext_template_description_1': 'test template description 1',
        'adtext_template_description_2': 'test template description 2',
        'campaign': campaign.id,
    }
    response = client.post(url, adtext_template_data)
    assert response.status_code == 302
    assert response.url == reverse('campaigns')
    AdTextTemplate.objects.get(**adtext_template_data)


# 2nd test for add template view
@pytest.mark.django_db
def test_025_add_adtext_template_get_logged_user(client, users):
    url = reverse('add_adtext_template')
    user = users[0]
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200


# 1st test for add adtext view
@pytest.mark.django_db
def test_009_add_adtext_post_logged_user(client, adgroups, users):
    url = reverse('add_adtext')
    user = users[0]
    client.force_login(user)
    adgroup = adgroups[0]
    adtext_data = {
        'adtext_headline_1': 'test headline 1',
        'adtext_headline_2': 'test headline 2',
        'adtext_description_1': 'test description 1',
        'adtext_description_2': 'test description 2',
        'adgroup': adgroup.id,
    }
    response = client.post(url, adtext_data)
    assert response.status_code == 302
    assert response.url == reverse('campaigns')
    AdText.objects.get(**adtext_data)


# 1st test for adgroup list view
@pytest.mark.django_db
def test_011_adgroup_list_view_logged_user(client, campaigns, users, adgroups):
    campaign = campaigns[0]
    url = reverse('adgroup_list', args=(campaign.id, ))
    user = users[0]
    client.force_login(user)
    response = client.get(url)
    adgroup_list = AdGroup.objects.filter(campaign=campaign.id)
    assert response.status_code == 200
    assert response.context['object_list'].count() == len(adgroup_list)


# 1st test for keywords & adtexts list view
@pytest.mark.django_db
def test_012_keywords_adtexts_list_view_logged_user(client, keywords, adgroups, users):
    adgroup = adgroups[0]
    url = reverse('keyword_list', args=(adgroup.id, ))
    user = users[0]
    client.force_login(user)
    response = client.get(url)
    keyword_list = Keyword.objects.filter(adgroup=adgroup.id)
    assert response.status_code == 200
    assert response.context['object_list'].count() == len(keyword_list)


# 1st test for campaign update view
@pytest.mark.django_db
def test_013_campaign_post_update_view_logged_user(client, campaigns, users):
    campaign = campaigns[0]
    url = reverse('update_campaign', args=(campaign.id, ))
    user = users[0]
    client.force_login(user)
    data = {
        'campaign_name': 'new campaign name',
        'user_id': user.id
    }
    response = client.post(url, data)
    assert response.status_code == 302
    Campaign.objects.get(campaign_name=data['campaign_name'])


# 1st test for adgroup update view
@pytest.mark.django_db
def test_014_adgroup_post_update_view_logged_user(client, campaigns, users, adgroups):
    campaign = campaigns[0]
    adgroup = adgroups[0]
    url = reverse('update_adgroup', args=(adgroup.id, ))
    user = users[0]
    client.force_login(user)
    data = {
        'adgroup_name': 'new adgroup name',
        'campaign': campaign.id
    }
    response = client.post(url, data)
    assert response.status_code == 302
    AdGroup.objects.get(adgroup_name=data['adgroup_name'])


# 1st test for keyword update view
@pytest.mark.django_db
def test_015_keyword_post_update_view_logged_user(client, keywords, users, adgroups):
    keyword = keywords[0]
    adgroup = adgroups[0]
    url = reverse('update_keyword', args=(keyword.id, adgroup.id,  ))
    user = users[0]
    client.force_login(user)
    data = {
        'keyword': 'new keyword name',
        'adgroup': adgroup.id
    }
    response = client.post(url, data)
    assert response.status_code == 302
    Keyword.objects.get(keyword=data['keyword'])


# 1st test for adtext update view
@pytest.mark.django_db
def test_016_adtext_post_update_view_logged_user(client, users, adgroups, adtexts):
    adgroup = adgroups[0]
    adtext = adtexts[0]
    url = reverse('update_adtext', args=(adtext.id, adgroup.id, ))
    user = users[0]
    client.force_login(user)
    data = {
        'adtext_headline_1': 'test headline1',
        'adtext_headline_2': 'test headline2',
        'adtext_description_1': 'test description 1',
        'adtext_description_2': 'test description 2',
        'adgroup': adgroup.id
    }
    response = client.post(url, data)
    assert response.status_code == 302
    AdText.objects.filter(adgroup=adgroup.id, adtext_headline_1=data['adtext_headline_1'])


# 1st test for adtext template update view
@pytest.mark.django_db
def test_017_adtext_template_post_update_view_logged_user(client, users, campaigns, adtext_templates):
    campaign = campaigns[0]
    adtext_template = adtext_templates[0]
    url = reverse('update_adtext_template', args=(adtext_template.id, ))
    user = users[0]
    client.force_login(user)
    data = {
        'adtext_template_headline_1': 'test template headline1',
        'adtext_template_headline_2': 'test template headline2',
        'adtext_template_description_1': 'test template description 1',
        'adtext_template_description_2': 'test template description 2',
        'campaign': campaign
    }
    response = client.post(url, data)
    assert response.status_code == 302
    AdTextTemplate.objects.filter(campaign=campaign.id, adtext_template_headline_1=data['adtext_template_headline_1'])


# 1st test for delete campaign view
@pytest.mark.django_db
def test_018_delete_campaign_post_logged_user(client, users, campaigns):
    campaign = campaigns[0]
    url = reverse('delete_campaign', args=(campaign.id, ))
    user = users[0]
    client.force_login(user)

    response = client.post(url)
    assert response.status_code == 302
    assert response.url == reverse('campaigns')
    assert len(campaigns) == 10
    assert Campaign.objects.all().count() == 9


# 1st test for delete adgroup view
@pytest.mark.django_db
def test_019_delete_adgroup_post_logged_user(client, users, campaigns, adgroups):
    campaign = campaigns[0]
    adgroup = adgroups[0]
    url = reverse('delete_adgroup', args=(adgroup.id, campaign.id, ))
    user = users[0]
    client.force_login(user)
    response = client.post(url)
    assert response.status_code == 302
    assert response.url == reverse('adgroup_list', args=(campaign.id, ))
    assert len(adgroups) == 10
    assert AdGroup.objects.all().count() == 9


# 1st test for delete keyword view
@pytest.mark.django_db
def test_020_delete_keyword_post_logged_user(client, users, keywords, adgroups):
    keyword = keywords[0]
    adgroup = adgroups[0]
    url = reverse('delete_keyword', args=(adgroup.id, keyword.id, ))
    user = users[0]
    client.force_login(user)
    response = client.post(url)
    assert response.status_code == 302
    assert response.url == reverse('keyword_list', args=(adgroup.id, ))
    assert len(keywords) == 10
    assert Keyword.objects.all().count() == 9


# 1st test for delete adtext view
@pytest.mark.django_db
def test_021_delete_adtext_post_logged_user(client, users, adtexts, adgroups):
    adtext = adtexts[0]
    adgroup = adgroups[0]
    url = reverse('delete_adtext', args=(adgroup.id, adtext.id, ))
    user = users[0]
    client.force_login(user)
    response = client.post(url)
    assert response.status_code == 302
    assert response.url == reverse('keyword_list', args=(adgroup.id, ))
    assert len(adtexts) == 10
    assert AdText.objects.all().count() == 9


@pytest.mark.django_db
def test_022_delete_adtext_template_post_logged_user(client, users, adtext_templates):
    adtext_template = adtext_templates[0]
    url = reverse('delete_template', args=(adtext_template.id, ))
    user = users[0]
    client.force_login(user)
    response = client.post(url)
    assert response.status_code == 302
    assert response.url == reverse('campaigns')
    assert len(adtext_templates) == 10
    assert AdTextTemplate.objects.all().count() == 9


