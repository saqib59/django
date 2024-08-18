# Generated by Django 5.1 on 2024-08-16 15:58

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChaiVarity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='chais')),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('chai_type', models.CharField(choices=[('ML', 'MASALA'), ('GR', 'GINGER'), ('PL', 'PLAIN'), ('EL', 'ELAICHI')], max_length=2)),
            ],
        ),
    ]
