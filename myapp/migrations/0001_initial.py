# Generated by Django 3.2.9 on 2022-01-02 12:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contestant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contestant_id', models.CharField(max_length=30, unique=True)),
                ('contestant_name', models.CharField(max_length=30)),
                ('contestant_image', models.ImageField(blank=True, null=True, upload_to='contestantimages/')),
                ('contestant_age', models.CharField(max_length=30)),
                ('contentant_height', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=30)),
                ('event_catagory', models.CharField(max_length=30)),
                ('event_image', models.ImageField(blank=True, null=True, upload_to='eventimages/')),
                ('event_startdate', models.CharField(max_length=30)),
                ('event_enddate', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Voted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_voted', models.BooleanField(default=False)),
                ('count', models.IntegerField(default=0)),
                ('contestant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.contestant')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='contestant',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.event'),
        ),
    ]
