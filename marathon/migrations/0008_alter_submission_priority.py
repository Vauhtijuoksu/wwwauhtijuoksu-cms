# Generated by Django 3.2.18 on 2024-01-22 19:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marathon', '0007_auto_20240118_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='priority',
            field=models.IntegerField(default=1, help_text='Jos ehdotat useampaa peliä (1=mieluisin)', validators=[django.core.validators.MinValueValidator(1)], verbose_name='tärkeysjärjestys'),
        ),
    ]
