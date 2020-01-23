# Generated by Django 2.2 on 2020-01-23 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20200123_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='identifiers',
            field=models.ManyToManyField(to='books.IndustryIdentifiers'),
        ),
        migrations.AlterField(
            model_name='book',
            name='released',
            field=models.DateField(verbose_name='release date'),
        ),
    ]
