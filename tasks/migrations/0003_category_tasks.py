# Generated by Django 4.1.5 on 2023-02-10 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='tasks',
            field=models.ManyToManyField(blank=True, to='tasks.task'),
        ),
    ]
