# Generated by Django 4.1.2 on 2022-10-09 06:36

import apps.geoposition.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jurisdictions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='ComingEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(db_index=True, max_length=100, verbose_name='Type of Event')),
                ('start_date', models.DateField(db_index=True, verbose_name='start date')),
                ('end_date', models.DateField(db_index=True, verbose_name='end date')),
                ('requirement', tinymce.models.HTMLField(verbose_name='Requirement to attend')),
                ('venue_name', models.CharField(max_length=50, verbose_name='Venue Name')),
                ('venue', apps.geoposition.fields.GeopositionField(max_length=42, verbose_name='venue')),
                ('is_featured', models.BooleanField(db_index=True, default=False, help_text='whether the event should be displayed in home page', verbose_name='is featured')),
                ('is_published', models.BooleanField(db_index=True, default=False, help_text='whether the event should be displayed', verbose_name='is published')),
                ('enable_registration', models.BooleanField(default=False, verbose_name='enable event registration')),
                ('registration_deadline_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='allow registration until')),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jurisdictions.county')),
            ],
            options={
                'verbose_name': 'Up coming event',
                'verbose_name_plural': 'Up coming events',
                'ordering': ['-start_date'],
                'permissions': [('can_publish_coming_events', 'Can publish coming events')],
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='department name')),
                ('description', models.TextField(verbose_name='description')),
                ('icon', models.CharField(max_length=100, verbose_name='icon')),
            ],
        ),
        migrations.CreateModel(
            name='ScoutingInBrief',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('content', tinymce.models.HTMLField(verbose_name='content')),
            ],
        ),
        migrations.CreateModel(
            name='SiteConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.SlugField(verbose_name='key')),
                ('value', models.CharField(max_length=200, verbose_name='value')),
            ],
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('image', models.ImageField(upload_to='Slides Images/%Y/%m', verbose_name='Slide Image')),
                ('featured', models.BooleanField(db_index=True, default=False, verbose_name='featured')),
                ('timestamp', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='timestamp')),
            ],
        ),
        migrations.CreateModel(
            name='WeProduce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('content', tinymce.models.HTMLField(verbose_name='content')),
                ('image', models.ImageField(upload_to='BackGround Images/%Y/%m', verbose_name='Background Image')),
            ],
        ),
        migrations.CreateModel(
            name='ScoutsCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_photo', models.ImageField(blank=True, null=True, upload_to='Scouts Centers/%Y', verbose_name='cover photo')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='camp center name')),
                ('camp_warden', models.CharField(db_index=True, max_length=50, verbose_name='camp warden')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('phone_number', models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(message="Entered mobile number isn't in a right format!", regex='^[0-9]{10,15}$')], verbose_name='phone number')),
                ('description', tinymce.models.HTMLField(blank=True, null=True, verbose_name='description')),
                ('services', tinymce.models.HTMLField(blank=True, null=True, verbose_name='services')),
                ('payments', tinymce.models.HTMLField(blank=True, null=True, verbose_name='payments')),
                ('exact_place', apps.geoposition.fields.GeopositionField(max_length=42, verbose_name='exact place')),
                ('sub_county', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jurisdictions.subcounty')),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last Name')),
                ('email', models.EmailField(help_text='example@gmail.com', max_length=254, unique=True, verbose_name='email')),
                ('phone_number', models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(message="Entered mobile number isn't in a right format!", regex='^[0-9]{10,15}$')], verbose_name='phone number')),
                ('message', models.TextField(blank=True, default='', verbose_name='Message')),
                ('event', models.ForeignKey(limit_choices_to=models.Q(('enable_registration', True), ('is_published', True)), on_delete=django.db.models.deletion.CASCADE, to='core.comingevent')),
                ('sub_county', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jurisdictions.subcounty')),
            ],
            options={
                'verbose_name': 'Event Registration',
            },
        ),
    ]
