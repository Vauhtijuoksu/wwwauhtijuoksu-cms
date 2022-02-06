# Generated by Django 3.0.14 on 2022-02-06 18:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start', models.DateField(blank=True, null=True)),
                ('end', models.DateField(blank=True, null=True)),
                ('reg_open', models.DateTimeField(blank=True, null=True)),
                ('reg_close', models.DateTimeField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=30)),
                ('discord', models.CharField(max_length=50)),
                ('twitch', models.CharField(blank=True, max_length=50)),
                ('allergies', models.TextField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_title', models.CharField(max_length=100)),
                ('publish_year', models.PositiveSmallIntegerField()),
                ('console', models.CharField(max_length=29)),
                ('console_display', models.CharField(max_length=29)),
                ('category', models.CharField(max_length=100)),
                ('estimate', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('video_link', models.URLField()),
                ('scoreboard_link', models.URLField()),
                ('time_constraints', models.TextField()),
                ('for_children', models.BooleanField(default=False)),
                ('flashing_lights', models.BooleanField(default=False)),
                ('hidden', models.BooleanField(default=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marathon.Event')),
                ('players', models.ManyToManyField(related_name='submissions', to='marathon.Player')),
            ],
        ),
    ]
