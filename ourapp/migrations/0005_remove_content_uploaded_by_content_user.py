# Generated by Django 5.0.2 on 2024-07-22 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourapp', '0004_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='uploaded_by',
        ),
        migrations.AddField(
            model_name='content',
            name='user',
            field=models.CharField(max_length=255, null=True),
        ),
    ]