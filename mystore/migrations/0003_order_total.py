# Generated by Django 3.2.5 on 2021-07-27 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystore', '0002_auto_20210727_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
