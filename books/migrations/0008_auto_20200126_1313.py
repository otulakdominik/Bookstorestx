# Generated by Django 2.2 on 2020-01-26 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20200123_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='identifiers',
            field=models.ManyToManyField(to='books.IndustryIdentifiers'),
        ),
    ]
