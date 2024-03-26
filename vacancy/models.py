from django.db import models
from django.contrib.auth import get_user_model
from users.models import Employer
from utils.models import BaseModel


class Category(BaseModel):
    title = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.title


class Company(BaseModel):
    name = models.CharField(max_length=128, unique=True)
    about = models.TextField()

    image = models.ImageField(upload_to='company', blank=True, null=True)

    def __str__(self):
        return self.name


class Vacancy(BaseModel):
    title = models.CharField(max_length=128)
    about = models.TextField()

    salary = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)

    is_published = models.BooleanField(default=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="vacancy")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="company")
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name="employer")

    def __str__(self):
        return self.title