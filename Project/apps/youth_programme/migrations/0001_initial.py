# Generated by Django 4.1.2 on 2022-10-09 06:36

import apps.core.project_requirements.utilities
import apps.geoposition.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registrations', '0001_initial'),
        ('jurisdictions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('section', models.CharField(choices=[('Sungura', 'Sungura'), ('Chipukizi', 'Chipukizi'), ('Mwamba', 'Mwamba'), ('Jasiri', 'Jasiri')], db_index=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='RM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report', models.FileField(upload_to='Youth Programme Department/%Y/%m', validators=[apps.core.project_requirements.utilities.validate_file_extension])),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('venue_name', models.CharField(max_length=50, verbose_name='Venue Name')),
                ('venue', apps.geoposition.fields.GeopositionField(max_length=42)),
                ('payments', models.BooleanField(db_index=True, default=False)),
                ('course_director', models.ForeignKey(help_text='Limited to active Scout Leaders with training level of PTC and above', limit_choices_to=apps.core.project_requirements.utilities.active_ptc_and_above_limit, on_delete=django.db.models.deletion.PROTECT, to='registrations.scoutleader')),
                ('director', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_director', to='registrations.scoutleader')),
                ('participants', models.ManyToManyField(limit_choices_to=models.Q(('active', True), ('section', 'Jasiri'), ('jasiri_investiture', True)), related_name='%(class)s_participants', to='registrations.scout')),
                ('staff', models.ManyToManyField(blank=True, related_name='%(class)s_staff', to='registrations.scoutleader')),
                ('sub_county', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jurisdictions.subcounty')),
                ('support_staff', models.ManyToManyField(help_text='Limited to only active Scout Leaders', limit_choices_to=apps.core.project_requirements.utilities.active_limit, related_name='%(class)s_trainers', to='registrations.scoutleader')),
                ('trainees', models.ManyToManyField(blank=True, related_name='%(class)s_trainees', to='registrations.scout')),
            ],
            options={
                'verbose_name': 'Rover Mate Course',
                'permissions': [('can_verify_Rover_Mate_payments', 'Can verify Rover Mate payments'), ('can_edit_Rover_Mate_trainees', 'Can edit Rover Mate Trainees')],
                'unique_together': {('venue_name', 'start_date', 'sub_county')},
            },
        ),
        migrations.CreateModel(
            name='PLC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report', models.FileField(upload_to='Youth Programme Department/%Y/%m', validators=[apps.core.project_requirements.utilities.validate_file_extension])),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('venue_name', models.CharField(max_length=50, verbose_name='Venue Name')),
                ('venue', apps.geoposition.fields.GeopositionField(max_length=42)),
                ('payments', models.BooleanField(db_index=True, default=False)),
                ('course_director', models.ForeignKey(help_text='Limited to active Scout Leaders with training level of PTC and above', limit_choices_to=apps.core.project_requirements.utilities.active_ptc_and_above_limit, on_delete=django.db.models.deletion.PROTECT, to='registrations.scoutleader')),
                ('director', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_director', to='registrations.scoutleader')),
                ('participants', models.ManyToManyField(limit_choices_to=apps.core.project_requirements.utilities.active_invested_limit, related_name='%(class)s_participants', to='registrations.scout')),
                ('staff', models.ManyToManyField(blank=True, related_name='%(class)s_staff', to='registrations.scoutleader')),
                ('sub_county', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jurisdictions.subcounty')),
                ('support_staff', models.ManyToManyField(help_text='Limited to only active Scout Leaders', limit_choices_to=apps.core.project_requirements.utilities.active_limit, related_name='%(class)s_trainers', to='registrations.scoutleader')),
                ('trainees', models.ManyToManyField(blank=True, related_name='%(class)s_trainees', to='registrations.scout')),
            ],
            options={
                'verbose_name': 'Patrol Leaders Course',
                'permissions': [('can_verify_PLC_payments', 'Can verify PLC payments'), ('can_edit_PLC_trainees', 'Can edit PLC Trainees')],
                'unique_together': {('venue_name', 'start_date', 'sub_county')},
            },
        ),
        migrations.CreateModel(
            name='ParkHoliday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report', models.FileField(upload_to='Youth Programme Department/%Y/%m', validators=[apps.core.project_requirements.utilities.validate_file_extension])),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('venue_name', models.CharField(max_length=50, verbose_name='Venue Name')),
                ('venue', apps.geoposition.fields.GeopositionField(max_length=42)),
                ('payments', models.BooleanField(db_index=True, default=False)),
                ('badges', models.ManyToManyField(limit_choices_to=models.Q(('section', 'Sungura')), to='youth_programme.badge')),
                ('director', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_director', to='registrations.scoutleader')),
                ('examiner', models.ForeignKey(help_text='Limited to active Scout Leaders with training level of PTC and above', limit_choices_to=apps.core.project_requirements.utilities.active_ptc_and_above_limit, on_delete=django.db.models.deletion.PROTECT, to='registrations.scoutleader')),
                ('participants', models.ManyToManyField(limit_choices_to=models.Q(('active', True), ('investiture', True), ('section', 'Sungura')), related_name='%(class)s_participants', to='registrations.scout')),
                ('staff', models.ManyToManyField(blank=True, related_name='%(class)s_staff', to='registrations.scoutleader')),
                ('sub_county', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jurisdictions.subcounty')),
                ('support_staff', models.ManyToManyField(help_text='Limited to only active Scout Leaders', limit_choices_to=apps.core.project_requirements.utilities.active_limit, related_name='%(class)s_trainers', to='registrations.scoutleader')),
                ('trainees', models.ManyToManyField(blank=True, related_name='%(class)s_trainees', to='registrations.scout')),
            ],
            options={
                'verbose_name': 'Park Holiday',
                'permissions': [('can_verify_ParkHoliday_payments', 'Can verify ParkHoliday payments'), ('can_edit_ParkHoliday_trainees', 'Can edit ParkHoliday Trainees')],
                'unique_together': {('venue_name', 'start_date', 'sub_county')},
            },
        ),
        migrations.CreateModel(
            name='Investiture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report', models.FileField(upload_to='Youth Programme Department/%Y/%m', validators=[apps.core.project_requirements.utilities.validate_file_extension])),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('venue_name', models.CharField(max_length=50, verbose_name='Venue Name')),
                ('venue', apps.geoposition.fields.GeopositionField(max_length=42)),
                ('payments', models.BooleanField(db_index=True, default=False)),
                ('director', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_director', to='registrations.scoutleader')),
                ('investor', models.ForeignKey(help_text='Limited to active Scout Leaders with training level of PTC and above', limit_choices_to=apps.core.project_requirements.utilities.active_ptc_and_above_limit, on_delete=django.db.models.deletion.PROTECT, to='registrations.scoutleader')),
                ('jasiri_participants', models.ManyToManyField(blank=True, limit_choices_to=models.Q(('active', True), ('section', 'Jasiri'), ('jasiri_investiture', False)), related_name='%(class)s_jasiri_participants', to='registrations.scout')),
                ('participants', models.ManyToManyField(blank=True, limit_choices_to=models.Q(('active', True), ('investiture', False), models.Q(('section', 'Sungura'), ('section', 'Chipukizi'), ('section', 'Mwamba'), _connector='OR')), related_name='%(class)s_participants', to='registrations.scout')),
                ('staff', models.ManyToManyField(blank=True, related_name='%(class)s_staff', to='registrations.scoutleader')),
                ('sub_county', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jurisdictions.subcounty')),
                ('support_staff', models.ManyToManyField(help_text='Limited to only active Scout Leaders', limit_choices_to=apps.core.project_requirements.utilities.active_limit, related_name='%(class)s_trainers', to='registrations.scoutleader')),
                ('trainees', models.ManyToManyField(blank=True, related_name='%(class)s_trainees', to='registrations.scout')),
            ],
            options={
                'permissions': [('can_verify_Investiture_payments', 'Can verify Investiture payments'), ('can_edit_Investiture_trainees', 'Can edit Investiture Trainees')],
                'unique_together': {('venue_name', 'start_date', 'sub_county')},
            },
        ),
        migrations.CreateModel(
            name='BadgeCamp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report', models.FileField(upload_to='Youth Programme Department/%Y/%m', validators=[apps.core.project_requirements.utilities.validate_file_extension])),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('venue_name', models.CharField(max_length=50, verbose_name='Venue Name')),
                ('venue', apps.geoposition.fields.GeopositionField(max_length=42)),
                ('payments', models.BooleanField(db_index=True, default=False)),
                ('director', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_director', to='registrations.scoutleader')),
                ('examiner', models.ForeignKey(help_text='Limited to active Scout Leaders with training level of PTC and above', limit_choices_to=apps.core.project_requirements.utilities.active_ptc_and_above_limit, on_delete=django.db.models.deletion.PROTECT, to='registrations.scoutleader')),
                ('kilele_participants', models.ManyToManyField(limit_choices_to=models.Q(('active', True), ('investiture', True), ('section', 'Mwamba'), ('mwanzo', 'True'), ('mwangaza', 'True'), ('kilele', 'False')), related_name='%(class)s_kilele_participants', to='registrations.scout')),
                ('mwangaza_participants', models.ManyToManyField(limit_choices_to=models.Q(('active', True), ('investiture', True), ('section', 'Mwamba'), ('mwanzo', 'True'), ('mwangaza', 'False')), related_name='%(class)s_mwangaza_participants', to='registrations.scout')),
                ('mwanzo_participants', models.ManyToManyField(limit_choices_to=models.Q(('active', True), ('investiture', True), ('section', 'Mwamba'), ('mwanzo', 'False')), related_name='%(class)s_mwanzo_participants', to='registrations.scout')),
                ('nyota_i_participants', models.ManyToManyField(limit_choices_to=models.Q(('active', True), ('investiture', True), ('section', 'Sungura'), ('nyota_i', 'False')), related_name='%(class)s_nyota_i_participants', to='registrations.scout')),
                ('nyota_ii_participants', models.ManyToManyField(limit_choices_to=models.Q(('active', True), ('investiture', True), ('section', 'Sungura'), ('nyota_i', 'True'), ('nyota_ii', 'False')), related_name='%(class)s_nyota_ii_participants', to='registrations.scout')),
                ('nyota_iii_participants', models.ManyToManyField(limit_choices_to=models.Q(('active', True), ('investiture', True), ('section', 'Sungura'), ('nyota_i', 'True'), ('nyota_ii', 'True'), ('nyota_iii', 'False')), related_name='%(class)s_nyota_iii_participants', to='registrations.scout')),
                ('shina_participants', models.ManyToManyField(limit_choices_to=models.Q(('active', True), ('investiture', True), ('section', 'Chipukizi'), ('zizi', 'True'), ('shina', 'False')), related_name='%(class)s_shina_participants', to='registrations.scout')),
                ('staff', models.ManyToManyField(blank=True, related_name='%(class)s_staff', to='registrations.scoutleader')),
                ('sub_county', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jurisdictions.subcounty')),
                ('support_staff', models.ManyToManyField(help_text='Limited to only active Scout Leaders', limit_choices_to=apps.core.project_requirements.utilities.active_limit, related_name='%(class)s_trainers', to='registrations.scoutleader')),
                ('tawi_participants', models.ManyToManyField(limit_choices_to=models.Q(('active', True), ('investiture', True), ('section', 'Chipukizi'), ('zizi', 'True'), ('shina', 'True'), ('tawi', 'False')), related_name='%(class)s_tawi_participants', to='registrations.scout')),
                ('trainees', models.ManyToManyField(blank=True, related_name='%(class)s_trainees', to='registrations.scout')),
                ('zizi_participants', models.ManyToManyField(limit_choices_to=models.Q(('active', True), ('investiture', True), ('section', 'Chipukizi'), ('zizi', 'False')), related_name='%(class)s_zizi_participants', to='registrations.scout')),
            ],
            options={
                'permissions': [('can_verify_BadgeCamp_payments', 'Can verify BadgeCamp payments'), ('can_edit_BadgeCamp_trainees', 'Can edit BadgeCamp Trainees')],
                'unique_together': {('venue_name', 'start_date', 'sub_county')},
            },
        ),
        migrations.CreateModel(
            name='BadgeCampStats',
            fields=[
            ],
            options={
                'verbose_name': 'Badge Camp Stats',
                'verbose_name_plural': 'Badge Camps Stats',
                'proxy': True,
                'default_permissions': ('view',),
                'indexes': [],
                'constraints': [],
            },
            bases=('youth_programme.badgecamp',),
        ),
        migrations.CreateModel(
            name='InvestitureStats',
            fields=[
            ],
            options={
                'verbose_name': 'Investiture Stats',
                'verbose_name_plural': 'Investitures Stats',
                'proxy': True,
                'default_permissions': ('view',),
                'indexes': [],
                'constraints': [],
            },
            bases=('youth_programme.investiture',),
        ),
        migrations.CreateModel(
            name='ParkHolidayStats',
            fields=[
            ],
            options={
                'verbose_name': 'Park Holiday Stats',
                'verbose_name_plural': 'Park Holiday Stats',
                'proxy': True,
                'default_permissions': ('view',),
                'indexes': [],
                'constraints': [],
            },
            bases=('youth_programme.parkholiday',),
        ),
        migrations.CreateModel(
            name='PLCStats',
            fields=[
            ],
            options={
                'verbose_name': 'PLC Stats',
                'verbose_name_plural': 'PLC Stats',
                'proxy': True,
                'default_permissions': ('view',),
                'indexes': [],
                'constraints': [],
            },
            bases=('youth_programme.plc',),
        ),
        migrations.CreateModel(
            name='RMStats',
            fields=[
            ],
            options={
                'verbose_name': 'Rover Mate Stats',
                'verbose_name_plural': 'Rover Mate Stats',
                'proxy': True,
                'default_permissions': ('view',),
                'indexes': [],
                'constraints': [],
            },
            bases=('youth_programme.rm',),
        ),
    ]