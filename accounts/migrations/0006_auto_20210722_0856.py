# Generated by Django 3.2.5 on 2021-07-22 08:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
        ('accounts', '0005_auto_20210719_0810'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_business',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_freelance',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to=None, verbose_name='Avatar')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('linkedin', models.URLField(blank=True, null=True, verbose_name='Linkedin Link')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Linkedin Link')),
                ('twitter', models.URLField(blank=True, null=True, verbose_name='Linkedin Link')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Linkedin Link')),
                ('behance', models.URLField(blank=True, null=True, verbose_name='Linkedin Link')),
                ('field', models.ManyToManyField(to='dashboard.Category')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
