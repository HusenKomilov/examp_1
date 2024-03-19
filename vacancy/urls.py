from django.urls import path
from vacancy import views

urlpatterns = [
    path("filter/<int:salary_from>/<int:salary_to>/", views.VacancyFilterListAPIView.as_view()),
    path("vacancy-count/", views.VacancyCountListAPIView.as_view()),
    path("company-count/", views.CompanyCountListAPIView.as_view()),
    path("worker-count/", views.CompanyCountListAPIView.as_view()),
    path("category-count/", views.CategoryPriceListAPIView.as_view()),
]
