from __future__ import unicode_literals

from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class Classroom(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class Student(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
