# Generated by Django 2.2.7 on 2019-12-03 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0007_auto_20191126_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]