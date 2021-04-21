# Generated by Django 3.2 on 2021-04-13 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='bio',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='owner',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='owner',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='owner',
            name='username',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
