# Generated by Django 4.0.6 on 2024-01-26 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_additionalresource_user_answer_user_attachment_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='is_submitted',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]