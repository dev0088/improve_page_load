# Generated by Django 2.1.7 on 2019-08-30 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bnboats_app', '0002_auto_20190814_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='mobile_code',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
