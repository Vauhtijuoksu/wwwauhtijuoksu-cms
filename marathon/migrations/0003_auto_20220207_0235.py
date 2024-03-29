# Generated by Django 3.0.14 on 2022-02-07 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marathon', '0002_auto_20220206_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='allergies',
            field=models.TextField(blank=True, verbose_name='erityisruokavalio'),
        ),
        migrations.AlterField(
            model_name='player',
            name='discord',
            field=models.CharField(max_length=50, verbose_name='discord-tunnus'),
        ),
        migrations.AlterField(
            model_name='player',
            name='nickname',
            field=models.CharField(max_length=30, verbose_name='nimimerkki'),
        ),
        migrations.AlterField(
            model_name='player',
            name='twitch',
            field=models.CharField(blank=True, max_length=50, verbose_name='twitch-tunnus'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='category',
            field=models.CharField(max_length=100, verbose_name='kategoria'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='console',
            field=models.CharField(max_length=29, verbose_name='laite/konsoli'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='console_display',
            field=models.CharField(blank=True, max_length=29, null=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='description',
            field=models.TextField(blank=True, verbose_name='perustelut'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='estimate',
            field=models.CharField(max_length=20, verbose_name='aika-arvio'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='flashing_lights',
            field=models.BooleanField(default=False, verbose_name='sisältää nopeasti vilkkuvia valoja'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='for_children',
            field=models.BooleanField(default=False, verbose_name='sopiva lapsille'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='game_title',
            field=models.CharField(max_length=100, verbose_name='peli'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='publish_year',
            field=models.CharField(max_length=10, verbose_name='julkaisuvuosi'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='scoreboard_link',
            field=models.URLField(blank=True, verbose_name='rankinglistalinkki'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='time_constraints',
            field=models.TextField(blank=True, verbose_name='aikataulurajoitteet'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='video_link',
            field=models.URLField(blank=True, verbose_name='videolinkki'),
        ),
    ]
