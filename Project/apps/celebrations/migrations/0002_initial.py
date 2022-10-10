# Generated by Django 4.1.2 on 2022-10-09 06:36

import apps.core.project_requirements.utilities
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registrations', '0001_initial'),
        ('jurisdictions', '0001_initial'),
        ('celebrations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='twobeadsaward',
            name='awardees',
            field=models.ManyToManyField(blank=True, related_name='%(class)s_awardees', to='registrations.scoutleader'),
        ),
        migrations.AddField(
            model_name='twobeadsaward',
            name='scout_leaders',
            field=models.ManyToManyField(blank=True, help_text='Only active Scout Leaders who have completed their WoodBadge Assessment are valid options', limit_choices_to=models.Q(('active', True), ('training', 'WB Assessment')), related_name='two_beads_awardees', to='registrations.scoutleader'),
        ),
        migrations.AddField(
            model_name='threebeadsaward',
            name='awardees',
            field=models.ManyToManyField(blank=True, related_name='%(class)s_awardees', to='registrations.scoutleader'),
        ),
        migrations.AddField(
            model_name='threebeadsaward',
            name='scout_leaders',
            field=models.ManyToManyField(blank=True, help_text='Only active Scout Leaders who have completed their ALT Project are valid options', limit_choices_to=models.Q(('active', True), ('training', 'ALT Project')), related_name='three_beads_awardees', to='registrations.scoutleader'),
        ),
        migrations.AddField(
            model_name='simbabadgeaward',
            name='awardees',
            field=models.ManyToManyField(blank=True, related_name='%(class)s_awardees', to='registrations.scout'),
        ),
        migrations.AddField(
            model_name='simbabadgeaward',
            name='mwamba_scouts',
            field=models.ManyToManyField(blank=True, help_text='Only active & invested Mwamba Scouts who have not yet been awarded Simba Badge Award are valid options', limit_choices_to=models.Q(('active', True), ('section', 'Mwamba'), ('investiture', True), ('simba_badge_award', False)), to='registrations.scout'),
        ),
        migrations.AddField(
            model_name='scoutleaderaward',
            name='awardees',
            field=models.ManyToManyField(blank=True, related_name='%(class)s_awardees', to='registrations.scoutleader'),
        ),
        migrations.AddField(
            model_name='scoutleaderaward',
            name='scout_leaders',
            field=models.ManyToManyField(blank=True, help_text='Only active Scout Leaders are valid options', limit_choices_to=apps.core.project_requirements.utilities.active_limit, to='registrations.scoutleader'),
        ),
        migrations.AddField(
            model_name='patronsday',
            name='chipukizi_awards',
            field=models.ManyToManyField(blank=True, limit_choices_to=apps.core.project_requirements.utilities.this_year_limit, to='celebrations.chuibadgeaward'),
        ),
        migrations.AddField(
            model_name='patronsday',
            name='county_participants',
            field=models.ManyToManyField(blank=True, limit_choices_to=apps.core.project_requirements.utilities.this_year_limit, to='celebrations.countyparticipants'),
        ),
        migrations.AddField(
            model_name='patronsday',
            name='jasiri_awards',
            field=models.ManyToManyField(blank=True, limit_choices_to=apps.core.project_requirements.utilities.this_year_limit, to='celebrations.chiefscoutaward'),
        ),
        migrations.AddField(
            model_name='patronsday',
            name='mwamba_awards',
            field=models.ManyToManyField(blank=True, limit_choices_to=apps.core.project_requirements.utilities.this_year_limit, to='celebrations.simbabadgeaward'),
        ),
        migrations.AddField(
            model_name='patronsday',
            name='scout_leaders_awards',
            field=models.ManyToManyField(blank=True, limit_choices_to=apps.core.project_requirements.utilities.this_year_limit, to='celebrations.scoutleaderaward'),
        ),
        migrations.AddField(
            model_name='patronsday',
            name='sungura_awards',
            field=models.ManyToManyField(blank=True, limit_choices_to=apps.core.project_requirements.utilities.this_year_limit, to='celebrations.linkbadgeaward'),
        ),
        migrations.AddField(
            model_name='linkbadgeaward',
            name='awardees',
            field=models.ManyToManyField(blank=True, related_name='%(class)s_awardees', to='registrations.scout'),
        ),
        migrations.AddField(
            model_name='linkbadgeaward',
            name='sungura_scouts',
            field=models.ManyToManyField(blank=True, help_text='Only active & invested Sungura Scouts who have not yet been awarded Link Badge Award are valid options', limit_choices_to=models.Q(('active', True), ('section', 'Sungura'), ('investiture', True), ('link_badge_award', False)), to='registrations.scout'),
        ),
        migrations.AddField(
            model_name='fourbeadsaward',
            name='awardees',
            field=models.ManyToManyField(blank=True, related_name='%(class)s_awardees', to='registrations.scoutleader'),
        ),
        migrations.AddField(
            model_name='fourbeadsaward',
            name='scout_leaders',
            field=models.ManyToManyField(blank=True, help_text='Only active Scout Leaders who have completed their ALT Project are valid options', limit_choices_to=models.Q(('active', True), ('training', 'LT Project')), related_name='four_beads_awardees', to='registrations.scoutleader'),
        ),
        migrations.AddField(
            model_name='founderee',
            name='camp_chief',
            field=models.ForeignKey(help_text='Only active Scout Leaders are valid options', limit_choices_to=apps.core.project_requirements.utilities.active_limit, on_delete=django.db.models.deletion.PROTECT, to='registrations.scoutleader'),
        ),
        migrations.AddField(
            model_name='founderee',
            name='county',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jurisdictions.county'),
        ),
        migrations.AddField(
            model_name='founderee',
            name='staff',
            field=models.ManyToManyField(related_name='%(class)s_staff', to='registrations.scoutleader'),
        ),
        migrations.AddField(
            model_name='founderee',
            name='support_staff',
            field=models.ManyToManyField(help_text='Only active Scout Leaders are valid options', limit_choices_to=apps.core.project_requirements.utilities.active_limit, related_name='%(class)s_support_staff', to='registrations.scoutleader'),
        ),
        migrations.AddField(
            model_name='countyparticipants',
            name='chipukizi_scouts',
            field=models.ManyToManyField(help_text='Only active Chipukizi Scouts are valid options', limit_choices_to=models.Q(('active', True), ('section', 'Chipukizi')), related_name='chipukizi_scouts', to='registrations.scout'),
        ),
        migrations.AddField(
            model_name='countyparticipants',
            name='county',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jurisdictions.county', unique_for_year='year'),
        ),
        migrations.AddField(
            model_name='countyparticipants',
            name='jasiri_scouts',
            field=models.ManyToManyField(help_text='Only active Jasiri Scouts are valid options', limit_choices_to=models.Q(('active', True), ('section', 'Jasiri')), to='registrations.scout'),
        ),
        migrations.AddField(
            model_name='countyparticipants',
            name='mwamba_scouts',
            field=models.ManyToManyField(help_text='Only active Mwamba Scouts are valid options', limit_choices_to=models.Q(('active', True), ('section', 'Mwamba')), related_name='mwamba_scouts', to='registrations.scout'),
        ),
        migrations.AddField(
            model_name='countyparticipants',
            name='scout_leaders',
            field=models.ManyToManyField(help_text='Only active Scout Leaders are valid options', limit_choices_to=apps.core.project_requirements.utilities.active_limit, to='registrations.scoutleader'),
        ),
        migrations.AddField(
            model_name='countyparticipants',
            name='scout_leaders_attendees',
            field=models.ManyToManyField(blank=True, related_name='%(class)s_scout_leaders_attendees', to='registrations.scoutleader'),
        ),
        migrations.AddField(
            model_name='countyparticipants',
            name='scouts_attendees',
            field=models.ManyToManyField(blank=True, related_name='%(class)s_scout_attendees', to='registrations.scout'),
        ),
        migrations.AddField(
            model_name='countyparticipants',
            name='sungura_scouts',
            field=models.ManyToManyField(help_text='Only active Sungura Scouts are valid options', limit_choices_to=models.Q(('active', True), ('section', 'Sungura')), related_name='sungura_scouts', to='registrations.scout'),
        ),
        migrations.AddField(
            model_name='chuibadgeaward',
            name='awardees',
            field=models.ManyToManyField(blank=True, related_name='%(class)s_awardees', to='registrations.scout'),
        ),
        migrations.AddField(
            model_name='chuibadgeaward',
            name='chipukizi_scouts',
            field=models.ManyToManyField(blank=True, help_text='Only active & invested Chipukizi Scouts who have not yet been awarded Chui Badge Award are valid options', limit_choices_to=models.Q(('active', True), ('section', 'Chipukizi'), ('investiture', True), ('chui_badge_award', False)), to='registrations.scout'),
        ),
        migrations.AddField(
            model_name='chiefscoutaward',
            name='awardees',
            field=models.ManyToManyField(blank=True, related_name='%(class)s_awardees', to='registrations.scout'),
        ),
        migrations.AddField(
            model_name='chiefscoutaward',
            name='jasiri_scouts',
            field=models.ManyToManyField(blank=True, help_text='Only active & invested Jasiri Scouts who have not yet been awarded Chief Scout Award (CSA) are valid options', limit_choices_to=models.Q(('active', True), ('section', 'Jasiri'), ('jasiri_investiture', True), ('csa_award', False)), to='registrations.scout'),
        ),
        migrations.CreateModel(
            name='FoundereeStats',
            fields=[
            ],
            options={
                'verbose_name': 'Founderee Stats',
                'verbose_name_plural': 'Founderees Stats',
                'proxy': True,
                'default_permissions': ('view',),
                'indexes': [],
                'constraints': [],
            },
            bases=('celebrations.founderee',),
        ),
        migrations.CreateModel(
            name='PatronsDayStats',
            fields=[
            ],
            options={
                'verbose_name': 'PatronsDay Stats',
                'verbose_name_plural': 'PatronsDay Stats',
                'proxy': True,
                'default_permissions': ('view',),
                'indexes': [],
                'constraints': [],
            },
            bases=('celebrations.patronsday',),
        ),
    ]