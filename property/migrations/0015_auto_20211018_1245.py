# Generated by Django 2.2.20 on 2021-10-18 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_auto_20211018_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='new_building',
            field=models.NullBooleanField(choices=[(True, 'да'), (False, 'нет'), (None, 'Неизвестно')], db_index=True, verbose_name='Новое здание'),
        ),
    ]