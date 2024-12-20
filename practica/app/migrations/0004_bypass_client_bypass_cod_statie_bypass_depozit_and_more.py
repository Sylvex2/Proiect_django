# Generated by Django 5.0.7 on 2024-08-19 08:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_bypass_observatii'),
    ]

    operations = [
        migrations.AddField(
            model_name='bypass',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.client'),
        ),
        migrations.AddField(
            model_name='bypass',
            name='cod_statie',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='bypass',
            name='depozit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.depozit'),
        ),
        migrations.AddField(
            model_name='bypass',
            name='info_statie',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bypass',
            name='particular',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.particular'),
        ),
        migrations.AddField(
            model_name='bypass',
            name='test',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.test'),
        ),
        migrations.AddField(
            model_name='client',
            name='cod_statie',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='info_statie',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='depozit',
            name='cod_statie',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='depozit',
            name='info_statie',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='particular',
            name='cod_statie',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='particular',
            name='info_statie',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='test',
            name='cod_statie',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='test',
            name='info_statie',
            field=models.TextField(blank=True, null=True),
        ),
    ]
