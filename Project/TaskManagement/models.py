from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    due_date = models.DateTimeField()
    status = models.CharField(max_length=15)
    user_id = models.IntegerField(null=False)
    
    class Meta:
        db_table = "TaskTable"

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = "UsersTable"


