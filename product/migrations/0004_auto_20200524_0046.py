# Generated by Django 2.2.9 on 2020-05-23 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
    ]
