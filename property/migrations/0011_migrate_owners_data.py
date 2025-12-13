from django.db import migrations
import phonenumbers


def migrate_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    flats = Flat.objects.all()

    print(f"\nНачинаю миграцию данных для {flats.count()} квартир...")

    for flat in flats.iterator():
        owner, created = Owner.objects.get_or_create(
            full_name=flat.owner,
            defaults={
                'phonenumber': flat.owners_phonenumber,
                'pure_phone': flat.owner_pure_phone,
            }
        )

        if not created:
            if owner.phonenumber != flat.owners_phonenumber:
                owner.phonenumber = flat.owners_phonenumber
                owner.pure_phone = flat.owner_pure_phone
                owner.save()

        if created:
            print(f"Создан новый собственник: {owner.full_name}")

    total_owners = Owner.objects.count()
    print(f"\n=== ИТОГ ===")
    print(f"Всего собственников в базе: {total_owners}")


def reverse_migration(apps, schema_editor):
    Owner = apps.get_model('property', 'Owner')
    Owner.objects.all().delete()
    print("Все собственники удалены")


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_owner'),
    ]

    operations = [
        migrations.RunPython(migrate_owners, reverse_migration),
    ]
