# Generated by Django 5.0.2 on 2024-07-22 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourapp', '0007_remove_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
