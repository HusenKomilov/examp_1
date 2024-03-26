from rest_framework import generics
from vacancy import serializers, models
from users.models import Worker
from django.db.models import Q, Count, Max, Min, Avg, Case, When

# 2-topshiriq
class VacancyFilterListAPIView(generics.ListAPIView):
    queryset = models.Vacancy.objects.all()
    serializer_class = serializers.VacancySerializer

    def get_queryset(self, **kwargs):
        return super().get_queryset().filter(
            (
                (
                    Q(salary__gte=self.kwargs['salary_from']) &
                    Q(salary__lte=self.kwargs['salary_to'])
                ) | (
                    Q(salary=self.kwargs['salary_from'])
                )
            ), is_published=True
        ).select_related("category", "company", "employer")


class VacancyCountListAPIView(generics.ListAPIView):
    serializer_class = serializers.VacancySerializer
    queryset = models.Vacancy.objects.filter(is_published=True)

    def get_queryset(self):
        return super().get_queryset().annotate(
            count=Count('title')
        ).select_related("category", "company", "employer")


class CompanyCountListAPIView(generics.ListAPIView):
    serializer_class = serializers.CompanySerializer
    queryset = models.Company.objects.all()

    def get_queryset(self):
        return super().get_queryset().annotate(count=Count("name"))


class WorkerCountListAPIView(generics.ListAPIView):
    serializer_class = serializers.WorkerSerializer
    queryset = Worker.objects.all()

    def get_queryset(self):
        return super().get_queryset().annotate(count=Count("resume"))


class CategoryPriceListAPIView(generics.ListAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategoryPriceSerializer

    def get_queryset(self):
        return super().get_queryset().annotate(
            count=Count("vacancy"),
            min=Min("vacancy__salary"),
            max=Max("vacancy__salary"),
            avg=Avg("vacancy__salary"),
        )
