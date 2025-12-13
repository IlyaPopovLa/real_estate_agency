from django.db import migrations
import phonenumbers


def normalize_phone_numbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')

    flats = Flat.objects.all()
    total = flats.count()
    processed = 0
    errors = 0

    for flat in flats.iterator():
        phone_number = flat.owners_phonenumber

        if phone_number and phone_number.strip():
            try:
                parsed_number = phonenumbers.parse(phone_number, 'RU')

                if phonenumbers.is_valid_number(parsed_number):
                    normalized_number = phonenumbers.format_number(
                        parsed_number,
                        phonenumbers.PhoneNumberFormat.E164
                    )
                    flat.owner_pure_phone = normalized_number
                    flat.save(update_fields=['owner_pure_phone'])
                    processed += 1
                else:
                    print(f"Некорректный номер для квартиры {flat.id}: {phone_number}")
                    flat.owner_pure_phone = None
                    flat.save(update_fields=['owner_pure_phone'])
                    errors += 1

            except phonenumbers.NumberParseException:
                print(f"Не удалось распарсить номер для квартиры {flat.id}: {phone_number}")
                flat.owner_pure_phone = None
                flat.save(update_fields=['owner_pure_phone'])
                errors += 1
        else:
            print(f"Пустой номер для квартиры {flat.id}")
            errors += 1

    print(f"\nОбработано квартир: {total}")
    print(f"Успешно: {processed}")
    print(f"Ошибок: {errors}")


def reverse_migration(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.all().update(owner_pure_phone=None)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.RunPython(normalize_phone_numbers, reverse_migration),
    ]