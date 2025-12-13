from django.db import migrations


def remove_old_fields(apps, schema_editor):
    print("Старые поля owner и owners_phonenumber остаются для обратной совместимости")
    print("Их можно удалить после тестирования")


def reverse_migration(apps, schema_editor):
    print("Восстановление старых полей не требуется")


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_fill_owner_flat_relations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owners_phonenumber',
        ),
    ]