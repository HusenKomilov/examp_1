from django.contrib import admin
from vacancy.models import Category, Company, Vacancy, Employer

admin.site.register(Category)
admin.site.register(Company)
admin.site.register(Vacancy)
admin.site.register(Employer)
