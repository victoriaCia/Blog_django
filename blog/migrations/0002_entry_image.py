# Generated by Django 4.1 on 2022-08-30 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='image',
            field=models.ImageField(default='blog/image-default.png', upload_to=''),
        ),
    ]
