from django.db import models

class Project(super, models.Model):
    name = models.CharField(max_length=250)

class Task(super, models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    