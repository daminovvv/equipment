# Generated by Django 4.2 on 2023-04-19 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eq_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]