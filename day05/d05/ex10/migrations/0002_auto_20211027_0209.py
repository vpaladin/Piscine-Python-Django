# Generated by Django 3.2.8 on 2021-10-26 23:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ex10', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='characters',
            field=models.ManyToManyField(null=True, to='ex10.People'),
        ),
        migrations.AlterField(
            model_name='movies',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='people',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='planets',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='planets',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
