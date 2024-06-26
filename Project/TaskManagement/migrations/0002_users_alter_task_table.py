# Generated by Django 5.0.6 on 2024-06-16 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskManagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'UsersTable',
            },
        ),
        migrations.AlterModelTable(
            name='task',
            table='TaskTable',
        ),
    ]
