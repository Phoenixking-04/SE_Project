# Generated by Django 5.1.5 on 2025-03-06 20:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('equipment', '0001_initial'),
        ('payments', '0001_initial'),
        ('sports', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, help_text='Number of equipment items booked (if applicable)', null=True)),
                ('booking_date', models.DateTimeField(auto_now_add=True)),
                ('equipment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookings', to='equipment.equipment')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='sports.location')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='accounts.user')),
            ],
        ),
        migrations.CreateModel(
            name='Confirmation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Confirmed', 'Confirmed'), ('Pending', 'Pending'), ('Failed', 'Failed')], default='Confirmed', max_length=20)),
                ('confirmation_date', models.DateTimeField(auto_now_add=True)),
                ('booking', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='confirmations', to='bookings.booking')),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='confirmations', to='payments.payment')),
                ('rental', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='confirmations', to='equipment.rental')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='confirmations', to='accounts.user')),
            ],
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('is_booked', models.BooleanField(default=False)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slots', to='sports.location')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='slot',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='bookings.slot'),
        ),
    ]
