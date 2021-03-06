# Generated by Django 2.2 on 2020-01-21 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='author')),
            ],
        ),
        migrations.CreateModel(
            name='industryIdentifiers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200, verbose_name='type')),
                ('identifier', models.CharField(max_length=200, verbose_name='identifier')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('released', models.DateField(verbose_name='release date')),
                ('pageCount', models.SmallIntegerField(blank=True, verbose_name='page count')),
                ('language', models.CharField(blank=True, max_length=100, verbose_name='language')),
                ('imageLink', models.URLField(blank=True, max_length=300, verbose_name='image link')),
                ('authors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Author')),
                ('identifiers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.industryIdentifiers')),
            ],
            options={
                'verbose_name': 'book',
                'verbose_name_plural': 'books',
            },
        ),
    ]
