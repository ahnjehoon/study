# Generated by Django 2.1.7 on 2019-06-19 01:42

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_introduce'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='posts/images'),
        ),
    ]
