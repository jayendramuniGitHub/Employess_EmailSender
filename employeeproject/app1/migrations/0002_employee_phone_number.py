# Generated by Django 5.0.6 on 2024-07-20 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='phone_number',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
