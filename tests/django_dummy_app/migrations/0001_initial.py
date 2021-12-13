# Generated by Django 3.2.8 on 2021-12-05 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('area', models.BigIntegerField()),
                ('population', models.BigIntegerField()),
                ('continent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='countries', to='django_dummy_app.continent')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
                ('source', models.TextField()),
                ('comment', models.TextField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='django_dummy_app.country')),
            ],
        ),
    ]