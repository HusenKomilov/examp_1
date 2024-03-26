from rest_framework import serializers
from vacancy import models
from users.models import Worker, Employer, User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ("id", "title")


class CompanySerializer(serializers.ModelSerializer):
    count = serializers.IntegerField(default=0)

    class Meta:
        model = models.Company
        fields = ("id", "name", "about", "count")


class VacancySerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    company = CompanySerializer()
    count = serializers.IntegerField(default=0)

    class Meta:
        model = models.Vacancy
        fields = ("id", "title", "about", "salary", "is_published", "category", "company", "count")


class WorkerSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField(default=0)

    class Meta:
        model = Worker
        fields = ("id", "user", "resume", "count")


class CategoryPriceSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField(default=0)
    min = serializers.DecimalField(max_digits=12, decimal_places=4)
    max = serializers.DecimalField(max_digits=12, decimal_places=4)
    avg = serializers.DecimalField(max_digits=12, decimal_places=4)

    # price = serializers.DecimalField(decimal_places=0, max_digits=9)

    class Meta:
        model = models.Category
        fields = ("title", "count", "min", "max", "avg")
