# Generated by Django 3.2.5 on 2021-07-10 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('color', models.TextField()),
                ('size', models.CharField(max_length=200)),
                ('item_detail', models.TextField()),
                ('description_model', models.TextField()),
                ('material_made', models.TextField()),
                ('image', models.CharField(max_length=400)),
            ],
        ),
    ]