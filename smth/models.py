from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    image = models.ImageField(upload_to='news_images')
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Controls (models.Model):
    image = models.ImageField(upload_to='teacher_images')
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Teacher(models.Model):
    image = models.ImageField(upload_to='teacher_images')
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def get_previous(self):
        teachers = Teacher.objects.filter(created_at__lt=self.created_at).order_by('-created_at')
        if teachers.exists():
            return teachers.first()
        return None

    def get_next(self):
        teachers = Teacher.objects.filter(created_at__gt=self.created_at).order_by('created_at')
        if teachers.exists():
            return teachers.first()
        return None

    previous = property(get_previous)
    next = property(get_next)

class Award(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='award_images')
    created_at = models.DateTimeField(auto_now_add=True)

class Contact(models.Model):
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    map_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

class Application(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    student_name = models.CharField(max_length=255)
    student_class = models.CharField(max_length=20)
    passport_data = models.TextField()
    parent_name = models.CharField(max_length=255)
    parent_passport_data = models.TextField()
    files = models.FileField(upload_to='applications')
    created_at = models.DateTimeField(auto_now_add=True)

class Question(models.Model):
    text = models.TextField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

class EducationalStandard(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class MaterialTechnicalSupport(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Scholarship(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class PaidService(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
