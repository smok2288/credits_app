from django.urls import path, include

from . import views

app_name = "contracts"

urlpatterns = [
    path('', views.home, name='home'),
    path("createcontract", views.createcontract, name="createcontract"),
    path("contracts-list", views.contract_list, name="contract_list"),
    path("manufacturers-list", views.manufacturers_list, name="manufacturers_list"),
    path("manufacturers-create", views.create_manufacturers, name="create_manufacturers"),
    path("products-list", views.products_list, name="products_list"),
    path("product-create", views.create_product, name="create_product"),
    path("loanrequests-list", views.loanrequests_list, name="loanrequests_list"),
    path("loanrequest-create", views.create_loanrequests, name="create_loanrequests"),
]
