# Generated by Django 4.0.1 on 2022-01-26 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0004_fuck'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuck',
            name='n',
            field=models.CharField(max_length=10, verbose_name='Fuck You Bitch!'),
        ),
    ]