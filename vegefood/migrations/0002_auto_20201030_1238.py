# Generated by Django 3.1.2 on 2020-10-30 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vegefood', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
