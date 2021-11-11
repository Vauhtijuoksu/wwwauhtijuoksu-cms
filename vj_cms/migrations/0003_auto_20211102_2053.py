# Generated by Django 3.2.8 on 2021-11-02 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('vj_cms', '0002_auto_20211012_2125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donatebar',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='vj_cms_donatebar', serialize=False, to='cms.cmsplugin')),
                ('goal', models.PositiveIntegerField(default=1000, verbose_name='Goal')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AlterField(
            model_name='gameinfo',
            name='estimate',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='estimate in seconds'),
        ),
    ]