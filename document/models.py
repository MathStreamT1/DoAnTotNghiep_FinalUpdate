from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from froala_editor.fields import FroalaField

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Document(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=100)
    content = FroalaField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
