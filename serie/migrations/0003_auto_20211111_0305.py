# Generated by Django 3.2.9 on 2021-11-11 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serie', '0002_episodio'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Serie',
            new_name='Anime',
        ),
        migrations.RenameField(
            model_name='comentario',
            old_name='serie',
            new_name='anime',
        ),
        migrations.RenameField(
            model_name='episodio',
            old_name='serieEpisodio',
            new_name='animeEpisodio',
        ),
    ]