from django.db import models

# Create your models here.
from .mixins import TimestampableMixin, StartEndDateMixin


class Manufacturer(TimestampableMixin, StartEndDateMixin):
    """Производители"""
    name = models.CharField("Производитель", max_length=250)

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"

    def __str__(self):
        return self.name


class Product(TimestampableMixin, StartEndDateMixin):
    """Товары"""
    name = models.CharField("Наименование товара", max_length=250)
    manufacturer = models.ForeignKey("Manufacturer", verbose_name="Производитель", related_name="product_manufacturer", on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Наименование товара"
        verbose_name_plural = "Наименование товаров"

    def __str__(self):
        return self.name


class Contract(TimestampableMixin, StartEndDateMixin):
    """Контракты"""
    number = models.IntegerField("Номер контракта", unique=True)

    class Meta:
        verbose_name = "Номер контракта"
        verbose_name_plural = "Номера контрактов"


class LoanRequest(TimestampableMixin, StartEndDateMixin):
    """Кредитные заявки"""
    contract = models.OneToOneField("Contract", verbose_name="Заявка на кредит", related_name="loan_contract", on_delete=models.SET_NULL, null=True)
    products = models.ManyToManyField("Product", verbose_name="Товары", related_name="loan_product")

    class Meta:
        verbose_name = "кредитная заявка"
        verbose_name_plural = "кредитные заявки"
