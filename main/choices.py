from django.db import models


class PartTimeChoice(models.TextChoices):
    FOR_fOUR_HOURS = 'FOR_fOUR_HOURS', 'От 4 часов в день'
    PART_DAY = 'PART_DAY', 'Неполный день'
    IN_EVENINGS = 'IN_EVENINGS', 'По вечерам'
    ON_WEEKDAYS = 'ON_WEEKDAYS', 'По выходным'
    ONE_TIME_TASK = 'ONE_TIME_TASK', 'Разовое задание'


class PriceTypeChoice(models.TextChoices):
    SUM = 'SUM', 'Sum'
    DOLLAR = 'DOLLAR', '$'
    EURO = 'EURO', '€'


class WorkScheduleChoice(models.TextChoices):
    FULL_DAY = 'FULL_DAY', 'Полный день'
    SHIFT_SH = 'SHIFT_SH', 'Сменный график '
    REMOTE = 'REMOTE', 'Удаленная работа'
    SHIFT_M = 'SHIFT_M', 'Вахтовый метод'
    FLEXIBLE = 'FLEXIBLE', 'Гибкий график'


class PublishChoice(models.TextChoices):
    PUBLISH_NOW = 'PUBLISH_NOW', 'Опубликовать сейчас'
    PUBLISH_ON_SCHEDULE = 'PUBLISH_ON_SCHEDULE', 'Опубликовать по расписанию'



