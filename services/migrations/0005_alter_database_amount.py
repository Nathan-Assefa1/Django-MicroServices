# Generated by Django 4.2.2 on 2023-12-12 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_client_rename_students_database'),
    ]

    operations = [
        migrations.AlterField(
            model_name='database',
            name='amount',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
