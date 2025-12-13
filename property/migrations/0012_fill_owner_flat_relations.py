from django.db import migrations


def fill_owner_flat_relations(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    flats = Flat.objects.all()
    processed = 0
    errors = 0

    print(f"\nНачинаю заполнение связей для {flats.count()} квартир...")

    for flat in flats.iterator():
        try:
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

            owner.flats.add(flat)
            processed += 1

            if processed % 100 == 0:
                print(f"Обработано {processed} квартир...")

        except Exception as e:
            print(f"Ошибка для квартиры {flat.id}: {e}")
            errors += 1

    print(f"\n=== ИТОГ ===")
    print(f"Обработано квартир: {processed}")
    print(f"Ошибок: {errors}")

    # Статистика
    owners_with_flats = Owner.objects.filter(flats__isnull=False).distinct().count()
    total_owners = Owner.objects.count()
    print(f"\nСобственников с квартирами: {owners_with_flats}/{total_owners}")


def reverse_migration(apps, schema_editor):
    Owner = apps.get_model('property', 'Owner')
    for owner in Owner.objects.all():
        owner.flats.clear()
    print("Все связи между собственниками и квартирами удалены")


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_migrate_owners_data'),
    ]

    operations = [
        migrations.RunPython(fill_owner_flat_relations, reverse_migration),
    ]
