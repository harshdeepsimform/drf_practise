# Generated by Django 3.2.4 on 2022-04-11 19:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('station', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('start_at', models.DateTimeField(null=True)),
                ('end_at', models.DateTimeField(null=True)),
                ('duration', models.IntegerField(verbose_name='Occupied Duration in hrs.')),
                ('status', models.IntegerField(choices=[(0, 'Ready'), (1, 'InProgress'), (2, 'Done'), (3, 'Cancel'), (4, 'Delay')], default=0)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='schedule', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Slot Number')),
                ('status', models.CharField(choices=[('A', 'Available'), ('O', 'Occupied')], default='A', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(default='India', max_length=100)),
                ('Longitude', models.DecimalField(decimal_places=10, max_digits=15, null=True)),
                ('Latitude', models.DecimalField(decimal_places=10, max_digits=15, null=True)),
                ('name', models.CharField(max_length=100, verbose_name='Station Name')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.AddField(
            model_name='slot',
            name='station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slots', to='station.station'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule_for', to='station.slot'),
        ),
    ]
