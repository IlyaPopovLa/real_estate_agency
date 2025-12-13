from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_add_owner_field'),
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
        migrations.AddField(
            model_name='flat',
            name='owners_phonenumber',
            field=models.CharField(
                'Номер владельца',
                max_length=20,
                blank=True,
                null=True,
                default=''
            ),
        ),
    ]
