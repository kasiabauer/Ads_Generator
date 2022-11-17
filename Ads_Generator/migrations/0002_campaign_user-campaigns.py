# Generated by Django 4.1.1 on 2022-11-17 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ads_Generator', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='campaign',
            constraint=models.UniqueConstraint(fields=('campaign_name', 'user'), name='user-campaigns'),
        ),
    ]