from rest_framework import serializers

from main import models


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.District
        fields = ('title',)


class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Industry
        fields = ('title',)


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('title', )


class VacancySerializer(serializers.ModelSerializer):
    industry = serializers.StringRelatedField(source="industry.title")
    specialization = serializers.StringRelatedField(source="specialization.title")
    # districts = DistrictSerializer()

    class Meta:
        model = models.Vacancy
        fields = ('specialization', 'from_price', 'to_price', 'industry')


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Skill
        fields = ('title',)


class VacancyDetailSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True)
    industry = serializers.StringRelatedField(source="industry.title")

    class Meta:
        model = models.Vacancy
        fields = (
            'title', 'from_price', 'to_price', 'price_type',
            'experience', 'description', 'skills', 'published_date'
        )


class VacancyListSerializer(serializers.ModelSerializer):
    districts = DistrictSerializer(many=True)
    experience = serializers.StringRelatedField(source="experience.title")

    class Meta:
        model = models.Vacancy
        fields = ('title', 'from_price', 'to_price', 'price_type',
                  'experience', 'industry', 'districts')


class SpecVacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Specialization
        fields = ()

