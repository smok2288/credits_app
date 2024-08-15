from django import forms

from . import models


class CreateContractForm(forms.ModelForm):

    class Meta:
        model = models.Contract
        fields = ("number",)


class CreateManufacturerForm (forms.ModelForm):

    class Meta:
        model = models.Manufacturer
        fields = ("name",)


class CreateProductForm (forms.ModelForm):

    class Meta:
        model = models.Product
        fields = ("name", "manufacturer")


class CreateLoanRequestsForm (forms.ModelForm):

    class Meta:
        model = models.LoanRequest
        fields = ("contract", "products")


class SearchManufacturerForm(forms.Form):
    number = forms.IntegerField(label="Id контракта", min_value=0, required=True)
