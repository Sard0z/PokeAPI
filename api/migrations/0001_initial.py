# Generated by Django 5.0 on 2023-12-13 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('image_url', models.CharField(max_length=200)),
            ],
        ),
    ]
