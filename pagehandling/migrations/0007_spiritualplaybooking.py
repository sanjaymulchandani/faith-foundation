# Generated by Django 4.1.3 on 2022-12-03 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagehandling', '0006_rename_contact_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpiritualPlayBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150)),
                ('mobile_number', models.CharField(max_length=15)),
                ('date_of_birth', models.DateField()),
                ('city', models.CharField(max_length=500)),
            ],
        ),
    ]