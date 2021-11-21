# Generated by Django 3.2.9 on 2021-11-21 16:17

import cloudinary.models
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('category', models.CharField(choices=[('documentary', 'DOCUMENTARY'), ('martial arts', 'MARTIAL ARTS'), ('historical', 'HISTORICAL'), ('adventure', 'ADVENTURE'), ('animation', 'ANIMATION'), ('thriller', 'THRILLER'), ('romance', 'ROMANCE'), ('fantasy', 'FANTASY'), ('horror', 'HORROR'), ('action', 'ACTION'), ('comedy', 'COMEDY'), ('sci-fi', 'SCI-FI'), ('drama', 'DRAMA')], max_length=21)),
                ('price', models.IntegerField(max_length=180)),
                ('Published', models.BooleanField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]