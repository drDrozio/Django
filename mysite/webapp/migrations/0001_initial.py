# Generated by Django 3.1 on 2020-08-27 07:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_category', models.CharField(max_length=200)),
                ('category_summary', models.CharField(max_length=200)),
                ('category_slug', models.CharField(default=1, max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='PostSeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_series', models.CharField(max_length=200)),
                ('post_summary', models.CharField(max_length=200)),
                ('post_category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='webapp.postcategory', verbose_name='Category')),
            ],
            options={
                'verbose_name_plural': 'Series',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=200)),
                ('post_text', models.TextField()),
                ('post_published', models.DateTimeField(default=datetime.datetime(2020, 8, 27, 12, 33, 29, 957748), verbose_name='date published')),
                ('post_slug', models.CharField(default=1, max_length=200)),
                ('post_series', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='webapp.postseries', verbose_name='Series')),
            ],
        ),
    ]