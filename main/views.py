from django.utils import timezone
from rest_framework import generics

from main import models
from main import serializers


class SpecVacancyListAPIView(generics.ListAPIView):
    queryset = models.Vacancy.objects.all()
    serializer_class = ...


class IndustryListAPIView(generics.ListAPIView):
    queryset = models.Industry.objects.all().order_by("?")[:12]
    serializer_class = serializers.IndustrySerializer


class FuturedInTashkentVacancyListAPIView(generics.ListAPIView):
    queryset = models.Vacancy.objects.filter(
        published_date=timezone.now().date(),
        districts__title='Tashkent',
    ).select_related("specialization", "industry").prefetch_related("districts")
    serializer_class = serializers.VacancySerializer


class SpecializationListAPIView(generics.ListAPIView):
    queryset = models.Specialization.objects.filter(parent=None)
    serializer_class = serializers.SpecializationSerializer


class VacancyDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Vacancy.objects.all().select_related("industry")
    serializer_class = serializers.VacancyDetailSerializer


class VacancyListAPIView(generics.ListAPIView):
    queryset = models.Vacancy.objects.all().prefetch_related("districts").select_related(
        "experience"
    )
    serializer_class = serializers.VacancyListSerializer
    filterset_fields = ('specialization', 'industry', 'experience', 'work_schedule', 'part_time')
    search_fields = ('title', 'skills__title')




