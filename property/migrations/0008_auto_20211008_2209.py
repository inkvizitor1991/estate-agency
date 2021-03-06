# Generated by Django 2.2.20 on 2021-10-08 16:07
import phonenumbers

from django.db import migrations


def format_phonenumbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        number = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        if phonenumbers.is_valid_number(number):
            flat.owner_pure_phone = phonenumbers.format_number(
                number,
                phonenumbers.PhoneNumberFormat.E164
            )
        else:
            flat.owner_pure_phone = 'Неверно указан номер'
        flat.save()


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0007_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.RunPython(format_phonenumbers),
    ]
