# Generated by Django 4.1.2 on 2022-10-09 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        ('registrations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comingevent',
            name='event_coordinators',
            field=models.ManyToManyField(blank=True, help_text='Only active Scout Leaders are valid options', limit_choices_to=models.Q(('active', True)), to='registrations.scoutleader'),
        ),
        migrations.CreateModel(
            name='ComingEventStats',
            fields=[
            ],
            options={
                'verbose_name': 'ComingEvent Stats',
                'verbose_name_plural': 'ComingEvents Stats',
                'proxy': True,
                'default_permissions': ('view',),
                'indexes': [],
                'constraints': [],
            },
            bases=('core.comingevent',),
        ),
        migrations.AlterUniqueTogether(
            name='scoutscenter',
            unique_together={('name', 'camp_warden', 'sub_county')},
        ),
        migrations.AlterUniqueTogether(
            name='comingevent',
            unique_together={('event_type', 'start_date', 'venue_name')},
        ),
    ]
