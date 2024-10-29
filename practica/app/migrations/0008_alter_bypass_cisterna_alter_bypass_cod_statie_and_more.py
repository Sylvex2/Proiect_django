# Generated by Django 5.0.7 on 2024-08-21 09:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_bypass_client_remove_bypass_depozit_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='bypass',
            name='cisterna',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cisterne'),
        ),
        migrations.AlterField(
            model_name='bypass',
            name='cod_statie',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='bypass',
            name='info_statie',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='bypass',
            name='motiv',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.motivebypass'),
        ),
        migrations.AlterField(
            model_name='bypass',
            name='observatii',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='bypass',
            name='sofer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.soferi'),
        ),
        migrations.AlterField(
            model_name='bypass',
            name='tip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tipuri'),
        ),
        migrations.AlterField(
            model_name='bypass',
            name='tip_statie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tipstatie'),
        ),
        migrations.AlterField(
            model_name='bypass',
            name='transportator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.transportatori'),
        ),
        migrations.AlterField(
            model_name='bypass',
            name='utilizator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]