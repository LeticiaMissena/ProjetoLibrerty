# Generated by Django 5.0.6 on 2024-06-04 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_livros_ano_remove_livros_numpaginas_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='livros',
            name='ano',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='livros',
            name='numPaginas',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='livros',
            name='sinopse',
            field=models.TextField(default='sem sinopse'),
            preserve_default=False,
        ),
    ]
