from django.db import models

# Create your models here.

class Task(models.Model):
    status_options = {
        0 : "To do",
        1 : "In Progress",
        2 : "Done"
    }
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    due_date = models.DateTimeField()
    status = models.IntegerField(default=0, choices=status_options)
    user_id = models.IntegerField(null=False)
    
    class Meta:
        db_table = "TaskTable"

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = "UsersTable"


