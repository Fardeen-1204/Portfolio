# Generated by Django 5.2 on 2025-05-05 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0002_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exp', models.IntegerField(max_length=100)),
                ('customer', models.IntegerField(max_length=100)),
                ('projects', models.IntegerField(max_length=100)),
            ],
        ),
    ]
