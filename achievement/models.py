from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from froala_editor.fields import FroalaField

class OLP(models.Model):

    RANK_CHOICES = [
        ('Vô địch', 'Vô địch'),
        ('Nhất', 'Nhất'),
        ('Nhì', 'Nhì'),
        ('Ba', 'Ba'),
        ('Khuyến khích', 'Khuyến khích'),
    ]
    rank = models.CharField(max_length=200, choices=RANK_CHOICES)
    description = models.TextField()
    khoa = models.TextField()
    SYSTEM_CHOICES = [
        ('Siêu Cúp', 'Hệ Siêu Cúp'),
        ('Chuyên Tin', 'Chuyên Tin Học'),
        ('Không Chuyên', 'Không Chuyên Tin Học'),
    ]
    system = models.CharField(max_length=200, choices=SYSTEM_CHOICES)

    YEAR_CHOICES = [(year, str(year)) for year in range(2015, 2066)]
    year = models.IntegerField(choices=YEAR_CHOICES)

    certificate = models.FileField(upload_to='certificates/', null=True, blank=True)

    def __str__(self):
        return f"OLP {self.description} - {self.rank} - {self.system} - {self.year}"

from django.db import models

class ICPC(models.Model):
    TEAM_SCOPE_CHOICES = [
        ('Khu Vực Miền Nam', 'Khu Vực Miền Nam'),
        ('Quốc Gia', 'Quốc Gia'),
        ('Asia', 'Asia'),
        ('Chung Kết Thế Giới', 'Chung Kết Thế Giới'),
    ]

    RESULT_CHOICES = [
        ('Vô Địch', 'Vô Địch'),
        ('Nhất', 'Nhất'),
        ('Nhì', 'Nhì'),
        ('Ba', 'Ba'),
        ('Khuyến Khích', 'Khuyến Khích'),
    ]

    team_name = models.TextField(max_length=255)
    khoa = models.TextField(null=True, blank=True)
    result = models.CharField(max_length=200, choices=RESULT_CHOICES)
    scope = models.CharField(max_length=200, choices=TEAM_SCOPE_CHOICES)
    
    YEAR_CHOICES = [(year, str(year)) for year in range(2015, 2066)]
    year = models.IntegerField(choices=YEAR_CHOICES)
    
    certificate = models.FileField(upload_to='certificates/', null=True, blank=True)

    def __str__(self):
        return f"{self.team_name} - {self.result} ({self.scope}) - {self.year} - {self.khoa}"

class PROCON(models.Model):

    RESULT_CHOICES = [
        ('Nhất', 'Nhất'),
        ('Nhì', 'Nhì'),
        ('Ba', 'Ba'),
        ('Khuyến Khích', 'Khuyến Khích'),
    ]
    
    YEAR_CHOICES = [(year, str(year)) for year in range(2015, 2066)]
    year = models.IntegerField(choices=YEAR_CHOICES)
    
    team_name = models.TextField(max_length=255)
    result = models.CharField(max_length=200, choices=RESULT_CHOICES)
    certificate = models.FileField(upload_to='certificates/', null=True, blank=True)
    
    def __str__(self):
        return f"{self.team_name} - {self.result}"