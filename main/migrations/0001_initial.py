# Generated by Django 3.0.3 on 2020-02-23 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Full title')),
                ('description', models.TextField(default='')),
                ('year', models.IntegerField(blank=True, null=True)),
                ('released', models.DateField(blank=True, null=True)),
                ('imdb', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('poster', models.ImageField(blank=True, null=True, upload_to='')),
                ('trailer_video', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
