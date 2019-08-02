from __future__ import unicode_literals


from django.db import models

class CourseManager(models.Manager):
    def validation(self, postData):
        errors = {}
        if len(postData['course_name']) <= 5:
            errors['course_name'] = "Name must be at least five characters."
        if len(postData['description']) <= 15:
            errors['description'] = "Description must be at least 15 characters"
        return errors

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    objects = CourseManager()