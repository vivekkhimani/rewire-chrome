# Generated by Django 3.2.9 on 2022-05-01 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RewireApp', '0004_flow'),
    ]

    operations = [
        migrations.AddField(
            model_name='flow',
            name='success',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]