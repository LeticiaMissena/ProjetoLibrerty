# Generated by Django 5.0.6 on 2024-06-04 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_livros_ano'),
    ]

    operations = [
        migrations.AddField(
            model_name='livros',
            name='ano',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]