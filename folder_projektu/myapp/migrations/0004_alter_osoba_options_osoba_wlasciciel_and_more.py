# Generated by Django 5.1.4 on 2025-01-07 10:07

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_stanowisko_osoba'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='osoba',
            options={'ordering': ['nazwisko'], 'permissions': [('view_person_other_owner', 'Pozwala zobaczyć modele Osoba innych właścicieli')]},
        ),
        migrations.AddField(
            model_name='osoba',
            name='wlasciciel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='osoba',
            name='data_dodania',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='person',
            name='pseudonim',
            field=models.CharField(default='', max_length=80),
        ),
    ]
