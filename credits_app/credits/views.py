from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from . import forms, models


def home(request):
    form = forms.SearchManufacturerForm(request.POST or None)
    context = {"form": form}
    if request.method == "POST" and form.is_valid():
        contract_id = request.POST.get('number')
        manufacturers = models.LoanRequest.objects.filter(contract_id=contract_id).exclude(
            products__manufacturer_id__isnull=True).values_list(
            'products__manufacturer_id', flat=True).distinct()
        if manufacturers:
            context["manufacturers"] = manufacturers
        else:
            context["error"] = "Не найдено ни одного производителя для данной кредитной заявки."
    return render(request, 'list.html', context)


def contract_list(request):
    contracts = models.Contract.objects.all()
    return render(request, "contract/list.html", {"contracts": contracts})


def createcontract(request):
    form = forms.CreateContractForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect(reverse("contracts:contract_list"))
    context = {"form": form}
    return render(request, "contract/create.html", context)


def create_manufacturers(request):
    form = forms.CreateManufacturerForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect(reverse("contracts:manufacturers_list"))
    context = {"form": form}
    return render(request, "manufacturer/create.html", context)


def manufacturers_list(request):
    manufacturers = models.Manufacturer.objects.all()
    return render(request, "manufacturer/list.html", {"manufacturers": manufacturers})


def products_list(request):
    products = models.Product.objects.all()
    return render(request, "product/list.html", {"products": products})


def create_product(request):
    form = forms.CreateProductForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect(reverse("contracts:products_list"))
    context = {"form": form}
    return render(request, "product/create.html", context)


def loanrequests_list(request):
    loanrequests = models.LoanRequest.objects.all()
    return render(request, "loanrequest/list.html", {"loanrequests": loanrequests})


def create_loanrequests(request):
    if models.Contract.objects.filter(loan_request__isnull=True):
        form = forms.CreateLoanRequestsForm(request.POST or None)
        context = {"form": form}
        if request.method == "POST" and form.is_valid():
            form.save()
            return redirect(reverse("contracts:loanrequests_list"))
    else:
        context = {"error": "Для контракта возможна только одна кредитная заявка. Пожалуйста, создайте новый контракт."}

    return render(request, "loanrequest/create.html", context)
