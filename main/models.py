from django.db import models
from django.contrib.auth import get_user_model

from utils.models import BaseModel
from main import choices


class Region(BaseModel):
    title = models.CharField(max_length=255)
    country = models.ForeignKey('self', on_delete=models.CASCADE,
                                related_name='regions', blank=True, null=True)

    def __str__(self):
        return self.title


class District(BaseModel):
    title = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.CASCADE,
                               related_name='districts')
    neighbour = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.title


class Specialization(BaseModel):
    title = models.CharField(max_length=255)
    # tags = models.ManyToManyField('Tag', related_name='specializations', blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE,
                               related_name='children', blank=True, null=True)

    def __str__(self):
        return self.title


# class Job(BaseModel):
#     title = models.CharField(max_length=255)
#     specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE,
#                                        related_name='jobs')
#
#     def __str__(self):
#         return self.title


class Experience(BaseModel):
    title = models.CharField(max_length=255)
    code = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title


class Industry(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()

    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title


class Skill(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


# class Tag(BaseModel):
#     title = models.CharField(max_length=255)
#     specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE,
#                                        related_name='tags')
#
#     def __str__(self):
#         return self.title


class Vacancy(BaseModel):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    from_price = models.IntegerField(blank=True, null=True)
    to_price = models.IntegerField(blank=True, null=True)
    price_type = models.CharField(max_length=10, choices=choices.PriceTypeChoice.choices,
                                  blank=True, null=True)

    # choices
    part_time = models.CharField(max_length=31, choices=choices.PartTimeChoice.choices,
                                 blank=True, null=True)
    work_schedule = models.CharField(max_length=31, choices=choices.WorkScheduleChoice.choices,
                                     blank=True, null=True)
    publish_type = models.CharField(max_length=63, choices=choices.PublishChoice.choices,
                                    default=choices.PublishChoice.PUBLISH_NOW)
    published_date = models.DateField(blank=True, null=True)
    published_time = models.TimeField(blank=True, null=True)

    # foreign key
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE,
                                   blank=True, null=True)

    # job = models.ForeignKey(Job, on_delete=models.CASCADE,
    #                         related_name='vacancies')
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE,
                                       related_name='vacancies')

    industry = models.ForeignKey(Industry, on_delete=models.CASCADE,
                                 related_name='vacancies')
    # many to mny
    # tags = models.ManyToManyField(Tag, related_name='vacancies', blank=True)
    districts = models.ManyToManyField(District, related_name='vacancies')

    skills = models.ManyToManyField(Skill, related_name='vacancies', blank=True)

    saved = models.ManyToManyField(get_user_model(),
                                   related_name='saved_vacancy', blank=True)

    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
