# Generated by Django 2.1.2 on 2018-12-02 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0002_auto_20181120_0145'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datao',
            old_name='content',
            new_name='xaxis',
        ),
        migrations.AddField(
            model_name='datao',
            name='yaxis',
            field=models.TextField(default='1 2 3 4 5'),
        ),
    ]
