# Generated by Django 3.2.5 on 2021-07-27 10:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='advister'),
        ),
    ]
