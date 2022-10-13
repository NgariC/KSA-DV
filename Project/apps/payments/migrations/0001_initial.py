# Generated by Django 4.1.2 on 2022-10-11 06:12

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registrations', '0002_alter_scout_email_alter_scout_investiture_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('youth_programme', '0002_alter_badge_name_alter_badge_section_and_more'),
        ('training', '0002_alter_alt_end_date_alter_alt_payments_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='C2BPayments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TransactionType', models.CharField(blank=True, max_length=12, null=True)),
                ('TransID', models.CharField(blank=True, max_length=12, null=True)),
                ('TransTime', models.CharField(blank=True, max_length=14, null=True)),
                ('TransAmount', models.CharField(blank=True, max_length=12, null=True)),
                ('BusinessShortCode', models.CharField(blank=True, max_length=6, null=True)),
                ('BillRefNumber', models.CharField(blank=True, max_length=20, null=True)),
                ('InvoiceNumber', models.CharField(blank=True, max_length=20, null=True)),
                ('OrgAccountBalance', models.CharField(blank=True, max_length=12, null=True)),
                ('ThirdPartyTransID', models.CharField(blank=True, max_length=20, null=True)),
                ('MSISDN', models.CharField(blank=True, max_length=12, null=True)),
                ('FirstName', models.CharField(blank=True, max_length=20, null=True)),
                ('MiddleName', models.CharField(blank=True, max_length=20, null=True)),
                ('LastName', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LNMOnline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CheckoutRequestID', models.CharField(blank=True, max_length=50, null=True)),
                ('MerchantRequestID', models.CharField(blank=True, max_length=20, null=True)),
                ('ResultCode', models.IntegerField(blank=True, null=True)),
                ('ResultDesc', models.CharField(blank=True, max_length=120, null=True)),
                ('Amount', models.FloatField(blank=True, null=True)),
                ('MpesaReceiptNumber', models.CharField(blank=True, max_length=15, null=True)),
                ('Balance', models.CharField(blank=True, max_length=12, null=True)),
                ('TransactionDate', models.DateTimeField(blank=True, null=True)),
                ('PhoneNumber', models.CharField(blank=True, max_length=13, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentsList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('ref_number', models.CharField(editable=False, max_length=16)),
                ('paid', models.BooleanField(db_index=True, default=False, verbose_name='Payments Done')),
                ('phone_number', models.CharField(help_text='The phone number will be used to make payments', max_length=13, validators=[django.core.validators.RegexValidator(message="Entered mobile number isn't in a right format!", regex='^[0-9]{10,15}$')])),
                ('badge_camps', models.ManyToManyField(blank=True, limit_choices_to=models.Q(('payments', False)), related_name='%(class)s_badge_camps', to='youth_programme.badgecamp')),
                ('badge_camps_paid_for', models.ManyToManyField(blank=True, to='youth_programme.badgecamp')),
                ('investitures', models.ManyToManyField(blank=True, limit_choices_to=models.Q(('payments', False)), related_name='%(class)s_investitures', to='youth_programme.investiture')),
                ('investitures_paid_for', models.ManyToManyField(blank=True, to='youth_programme.investiture')),
                ('itcs', models.ManyToManyField(blank=True, limit_choices_to=models.Q(('payments', False)), related_name='%(class)s_itcs', to='training.itc')),
                ('itcs_paid_for', models.ManyToManyField(blank=True, to='training.itc')),
                ('park_holidays', models.ManyToManyField(blank=True, limit_choices_to=models.Q(('payments', False)), related_name='%(class)s_park_holidays', to='youth_programme.parkholiday')),
                ('park_holidays_paid_for', models.ManyToManyField(blank=True, to='youth_programme.parkholiday')),
                ('plcs', models.ManyToManyField(blank=True, limit_choices_to=models.Q(('payments', False)), related_name='%(class)s_plcs', to='youth_programme.plc')),
                ('plcs_paid_for', models.ManyToManyField(blank=True, to='youth_programme.plc')),
                ('ptcs', models.ManyToManyField(blank=True, limit_choices_to=models.Q(('payments', False)), related_name='%(class)s_ptcs', to='training.ptc')),
                ('ptcs_paid_for', models.ManyToManyField(blank=True, to='training.ptc')),
                ('rover_mates', models.ManyToManyField(blank=True, limit_choices_to=models.Q(('payments', False)), related_name='%(class)s_rover_mates', to='youth_programme.rm')),
                ('rover_mates_paid_for', models.ManyToManyField(blank=True, to='youth_programme.rm')),
                ('scout_leaders', models.ManyToManyField(blank=True, limit_choices_to=models.Q(('active', False)), related_name='%(class)s_scout_leaders', to='registrations.scoutleader')),
                ('scout_leaders_paid_for', models.ManyToManyField(blank=True, to='registrations.scoutleader')),
                ('scouts', models.ManyToManyField(blank=True, limit_choices_to=models.Q(('active', False)), related_name='%(class)s_scout', to='registrations.scout')),
                ('scouts_paid_for', models.ManyToManyField(blank=True, to='registrations.scout')),
                ('units', models.ManyToManyField(blank=True, limit_choices_to=models.Q(('active', False)), related_name='%(class)s_units', to='registrations.unit')),
                ('units_paid_for', models.ManyToManyField(blank=True, to='registrations.unit')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
