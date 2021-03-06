# Generated by Django 3.2.9 on 2021-11-21 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soko', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='slug',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('External Works', (('Gates', 'GATES'), ('Landscaping', 'LANDSCAPING'), ('Fences', 'FENCES'))), ('Fittings and Furnishings', (('Equipments', 'EQUIPMENTS'), ('Furnitures', 'FURNITURES'))), ('Genearal Finishes', (('Paints', 'PAINTS'),)), ('Internal Finishes', (('Floor Finishes', 'FLOOR FINISHES'), ('Tiles', 'TILES'))), ('Structure', 'STRUCTURE'), ('Superstructure', (('Glass', 'GATES'), ('Openings', 'OPENINGS'), ('Railing', 'RAILINGS'))), ('Taps', 'TAPS'), ('Tools and Equipment', 'TOOLS & EQUIPMENTS')], max_length=55),
        ),
        migrations.AlterField(
            model_name='product',
            name='condition',
            field=models.CharField(choices=[('New', 'NEW'), ('Used', 'USED'), ('Manufacturer Refurbished', 'MANUFACTURER REFURBISHED'), ('For Parts & Not Working', 'FOR PARTS & NOT WORKING')], max_length=55),
        ),
    ]
