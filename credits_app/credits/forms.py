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
    loan_request = forms.ModelChoiceField(queryset=models.LoanRequest.objects.all(), required=False)

    class Meta:
        model = models.Product
        fields = ("name", "manufacturer", "loan_request")


class CreateLoanRequestsForm (forms.ModelForm):
    contract = forms.ModelChoiceField(queryset=models.Contract.objects.filter(loan_request__isnull=True))

    class Meta:
        model = models.LoanRequest
        fields = ("number", "contract",)


class SearchManufacturerForm(forms.Form):
    number = forms.IntegerField(label="Id контракта", min_value=0, required=True)
