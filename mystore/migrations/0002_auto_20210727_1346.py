# Generated by Django 3.2.5 on 2021-07-27 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(max_length=1000)),
                ('name', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=1000)),
                ('address2', models.CharField(max_length=1000)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('zipcode', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.CharField(max_length=200),
        ),
    ]
