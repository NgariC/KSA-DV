# Generated by Django 4.1.3 on 2022-11-11 18:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_payments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payments',
            old_name='timestamp',
            new_name='date_created',
        ),
        migrations.AddField(
            model_name='payments',
            name='amount_paid',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payments',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='payments',
            name='paid',
            field=models.BooleanField(db_index=True, default=False, verbose_name='Payments Done'),
        ),
        migrations.AddField(
            model_name='payments',
            name='phone_number',
            field=models.CharField(default=1, help_text='The phone number will be used to make payments', max_length=13, validators=[django.core.validators.RegexValidator(message="Entered mobile number isn't in a right format!", regex='^[0-9]{10,15}$')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payments',
            name='ref_number',
            field=models.CharField(default=1, editable=False, max_length=16),
            preserve_default=False,
        ),
    ]
