# Generated by Django 5.1.5 on 2025-03-12 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Price for this specific membership instance.', max_digits=8, null=True),
        ),
    ]
