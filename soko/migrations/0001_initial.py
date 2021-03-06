# Generated by Django 3.2.9 on 2021-11-21 20:02

import cloudinary.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('category', models.CharField(choices=[('External Works', (('Gates', 'GATES'), ('Landscaping', 'LANDSCAPING'), ('Fences', 'FENCES'))), ('Fittings and Furnishings', (('Equipments', 'EQUIPMENTS'), ('Furnitures', 'FURNITURES'))), ('Genearal Finishes', (('Paints', 'PAINTS'),)), ('Internal Finishes', (('Floor Finishes', 'FLOOR FINISHES'), ('Tiles', 'TILES'))), ('Structure', 'STRUCTURE'), ('Superstructure', (('Glass', 'GATES'), ('Openings', 'LANDSCAPING'), ('Railing', 'FENCES'))), ('Taps', 'TAPS'), ('Tools and Equipment', 'TOOLS & EQUIPMENTS')], max_length=55)),
                ('price', models.IntegerField(default=0)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(choices=[('Buy', 'BUY'), ('Rent', 'RENT')], max_length=55)),
                ('condition', models.CharField(choices=[('New', 'BUY'), ('Used', 'RENT'), ('Manufacturer Refurbished', 'MANUFACTURER REFURBISHED'), ('For Parts & Not Working', 'FOR PARTS & NOT WORKING')], max_length=55)),
                ('view', models.IntegerField(default=0)),
                ('description', models.TextField(max_length=1000)),
                ('location', models.CharField(max_length=200)),
                ('precise_location', models.CharField(max_length=200)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('negotiatable', models.BooleanField(default=False)),
                ('agreement', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_post', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_ratings', to='soko.product')),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(blank=True, max_length=30, null=True)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
                ('wished_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='soko.product')),
            ],
        ),
        migrations.CreateModel(
            name='VendorProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(blank=True, max_length=150, null=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('gender', models.CharField(choices=[('Male', 'MALE'), ('Female', 'FEMALE'), ('Other', 'OTHER')], max_length=55)),
                ('location', models.CharField(max_length=55)),
                ('bio', models.TextField(max_length=120, null=True)),
                ('avatar', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('youtube', models.URLField(blank=True, max_length=250, null=True)),
                ('facebook', models.URLField(blank=True, max_length=250, null=True)),
                ('linkedin', models.URLField(blank=True, max_length=250, null=True)),
                ('twitter', models.URLField(blank=True, max_length=250, null=True)),
                ('instagram', models.URLField(blank=True, max_length=250, null=True)),
                ('website', models.URLField(blank=True, max_length=250, null=True)),
                ('is_vendor', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('purchased', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comment', to='soko.product')),
                ('rating', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_ratings', to='soko.rating')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
