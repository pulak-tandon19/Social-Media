# Generated by Django 4.0.1 on 2022-01-26 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fuck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n', models.CharField(max_length=10)),
            ],
        ),
    ]