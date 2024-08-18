from django.db import models

from .mixins import TimestampableMixin, StartEndDateMixin


class LoanRequest(TimestampableMixin, StartEndDateMixin):
    """Кредитные заявки"""
    number = models.CharField("Номер кредитной заявки", max_length=250)
    contract = models.OneToOneField("Contract", verbose_name="Контракт", related_name="loan_request",
                                    on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Кредитная заявка"
        verbose_name_plural = "Кредитные заявки"

    def __str__(self):
        return self.number


class Contract(TimestampableMixin, StartEndDateMixin):
    """Контракты"""
    number = models.IntegerField("Номер контракта", unique=True)

    class Meta:
        verbose_name = "Номер контракта"
        verbose_name_plural = "Номера контрактов"

    def __str__(self):
        return f"Контракт №{self.number}"


class Product(TimestampableMixin, StartEndDateMixin):
    """Товары"""
    name = models.CharField("Наименование товара", max_length=250)
    loan_request = models.ForeignKey("LoanRequest", verbose_name="Кредитная заявка", related_name="products",
                                     on_delete=models.CASCADE, blank=True, null=True)
    manufacturer = models.ForeignKey("Manufacturer", verbose_name="Производитель", related_name="products",
                                     on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Наименование товара"
        verbose_name_plural = "Наименование товаров"

    def __str__(self):
        return self.name


class Manufacturer(TimestampableMixin, StartEndDateMixin):
    """Производители"""
    name = models.CharField("Производитель", max_length=250)

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"

    def __str__(self):
        return self.name
