# Generated by Django 5.0.7 on 2024-07-27 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='recipe_image',
            field=models.ImageField(upload_to='recipes_images/'),
        ),
    ]
