# Generated by Django 4.2.2 on 2023-12-11 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_students_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students',
            old_name='first_name',
            new_name='date_of_transaction',
        ),
        migrations.RenameField(
            model_name='students',
            old_name='last_name',
            new_name='user_email',
        ),
        migrations.RemoveField(
            model_name='students',
            name='file',
        ),
        migrations.RemoveField(
            model_name='students',
            name='marks',
        ),
        migrations.RemoveField(
            model_name='students',
            name='roll_number',
        ),
        migrations.RemoveField(
            model_name='students',
            name='section',
        ),
        migrations.AddField(
            model_name='students',
            name='amount',
            field=models.FloatField(null=True),
        ),
    ]
