# Generated by Django 5.0.3 on 2024-04-02 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_plantain_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantain',
            name='image_url',
            field=models.URLField(),
        ),
    ]