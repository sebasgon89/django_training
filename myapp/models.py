from django.db import models

class Project(super, models.Model):
    name = models.CharField(max_length=250)
