# Generated by Django 2.2.3 on 2019-08-11 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0001_squashed_20200219'),
        ('style', '0006_auto_20190809_1757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='olddocumentstyle',
            name='fonts',
        ),
        migrations.DeleteModel(
            name='DocumentFont',
        ),
        migrations.DeleteModel(
            name='OldDocumentStyle',
        ),
    ]
