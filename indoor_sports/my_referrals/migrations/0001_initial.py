# Generated by Django 5.1.5 on 2025-03-12 00:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friend_email', models.EmailField(blank=True, help_text='Email address of the friend being referred', max_length=254, null=True)),
                ('points_earned', models.IntegerField(default=0)),
                ('redeemed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('referred_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='referrals_received', to=settings.AUTH_USER_MODEL)),
                ('referrer_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='referrals_given', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
