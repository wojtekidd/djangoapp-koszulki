# Generated by Django 3.0.3 on 2020-02-29 11:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='stars',
            field=models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
