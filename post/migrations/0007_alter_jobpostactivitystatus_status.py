# Generated by Django 4.0.6 on 2022-07-22 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_jobpostactivitystatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpostactivitystatus',
            name='status',
            field=models.CharField(choices=[('writing', 'writing'), ('submitted', 'submitted'), ('under_review', 'under_review'), ('interview_planned', 'interview_planned'), ('in_recruitment_progress', 'in_recruitment_progress')], max_length=128),
        ),
    ]
