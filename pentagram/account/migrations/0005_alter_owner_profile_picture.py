# Generated by Django 3.2 on 2021-04-20 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_owner_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='profile_picture',
            field=models.ImageField(default='user.png', upload_to='image/user'),
        ),
    ]
