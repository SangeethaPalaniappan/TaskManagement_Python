# Generated by Django 5.0.6 on 2024-06-16 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskManagement', '0006_alter_task_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
