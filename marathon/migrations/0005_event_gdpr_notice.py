# Generated by Django 3.2.12 on 2022-03-23 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marathon', '0004_auto_20220323_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='gdpr_notice',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Tietosuojaseloste'),
        ),
    ]