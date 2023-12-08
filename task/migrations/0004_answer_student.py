# Generated by Django 4.2.7 on 2023-12-08 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
        ('task', '0003_task_views_by_alter_task_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answer_list', to='students.student'),
        ),
    ]