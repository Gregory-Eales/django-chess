# Generated by Django 3.0.1 on 2019-12-21 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chess', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('space', models.ImageField(upload_to='')),
            ],
        ),
    ]
