# Generated by Django 3.1.6 on 2021-02-06 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20210131_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorreservationreception',
            name='day_of_the_week',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='doctorreservationreception',
            name='frequency',
            field=models.JSONField(blank=True, null=True),
        ),
    ]