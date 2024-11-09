# Generated by Django 5.1.3 on 2024-11-09 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthdash', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercred',
            name='bloodgroup',
            field=models.CharField(default=1, max_length=40),
        ),
        migrations.AddField(
            model_name='usercred',
            name='guardian',
            field=models.CharField(default=1, max_length=40),
        ),
        migrations.AddField(
            model_name='usercred',
            name='guardphn',
            field=models.CharField(default=1, max_length=20),
        ),
        migrations.AddField(
            model_name='usercred',
            name='health',
            field=models.CharField(default=1, max_length=40),
        ),
        migrations.AddField(
            model_name='usercred',
            name='insurance',
            field=models.CharField(default=1, max_length=40),
        ),
        migrations.AddField(
            model_name='usercred',
            name='name',
            field=models.CharField(default=1, max_length=40),
        ),
        migrations.AddField(
            model_name='usercred',
            name='phone',
            field=models.CharField(default=1, max_length=20),
        ),
    ]