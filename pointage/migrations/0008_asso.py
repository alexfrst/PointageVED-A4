# Generated by Django 3.0.3 on 2020-09-14 08:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('pointage', '0007_auto_20200911_2138'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asso',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('value', models.CharField(choices=[('A', 'Atelier'), ('B', "Bureau d'étude"), ('D', 'Découpe laser')], default='', max_length=8)),
            ],
        ),
    ]
