# Generated by Django 2.2.1 on 2019-09-25 10:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rendez_vous_web', '0003_auto_20190829_0413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rendez_vous',
            name='eleve',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='rendez_vous',
            name='enseignant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]
