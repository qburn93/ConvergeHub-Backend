# Generated by Django 3.2.18 on 2023-03-19 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20230319_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../default_profile_bhadqa', upload_to='images/'),
        ),
    ]
