# Generated by Django 5.0.1 on 2024-01-10 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='job_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Qualification', models.CharField(max_length=150)),
                ('required_skills', models.CharField(max_length=150)),
                ('experiences_required', models.CharField(max_length=30)),
                ('vacancies', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=150)),
                ('application_deadline', models.CharField(max_length=150)),
            ],
        ),
    ]
