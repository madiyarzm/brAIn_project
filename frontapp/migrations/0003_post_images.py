# Generated by Django 5.0.7 on 2024-07-22 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontapp', '0002_alter_post_options_post_created_on_post_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
