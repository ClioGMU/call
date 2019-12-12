# Generated by Django 2.2.7 on 2019-11-26 20:01

from django.db import migrations
import django.utils.timezone
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0005_auto_20191126_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='name',
            field=django_countries.fields.CountryField(default=django.utils.timezone.now, max_length=2),
            preserve_default=False,
        ),
    ]
