import datetime

from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q, QuerySet
from django.urls import reverse
from django.utils import timezone


class TimestampableMixin(models.Model):
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата редактирования", blank=True, null=True)

    class Meta:
        abstract = True

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.updated_at = timezone.now()
        return super().save(
            force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields
        )


class ActiveManager(models.Manager):
    @staticmethod
    def get_query(related_key="") -> Q:
        related_key += "__" if related_key else ""
        day_today: datetime = datetime.date.today()
        return Q(**{f"{related_key}start_date__lte": day_today}) & ~Q(**{f"{related_key}end_date__lte": day_today})

    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(self.get_query())


class StartEndDateMixin(models.Model):
    start_date = models.DateField("Дата ввода записи", default=timezone.now)
    end_date = models.DateField("Дата деактивации записи", blank=True, null=True)

    objects = models.Manager()
    active_objects = ActiveManager()

    class Meta:
        abstract = True
        default_manager_name = "objects"

    def clean_fields(self, exclude=None):
        super().clean_fields(exclude)
        if self.end_date and self.end_date < self.start_date:
            raise ValidationError({"end_date": ["Дата деактивации не должна быть меньше даты ввода"]})


def constant_messages(request):
    return {
        "DELETE_CONFIRM_MSG": "Вы действительно хотите удалить эту запись?",
        "NO_RECORDS": "Записей нет",
        "BACK_URL": request.META.get("HTTP_REFERER", None) or reverse("contracts:home"),
    }