# Generated by Django 4.0 on 2023-08-18 02:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('saidas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='saida',
            options={'ordering': ['-dt_saida']},
        ),
        migrations.AddField(
            model_name='saida',
            name='dt_saida',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]