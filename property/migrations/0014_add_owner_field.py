from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_remove_old_owner_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='owner',
            field=models.CharField(
                'ФИО владельца',
                max_length=200,
                blank=True,
                null=True,
                default=''
            ),
        ),
    ]
