# Generated by Django 4.2.20 on 2025-03-17 06:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0005_review_dislikes_review_likes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='reports',
            field=models.ManyToManyField(blank=True, related_name='reported_reviews', to=settings.AUTH_USER_MODEL),
        ),
    ]
