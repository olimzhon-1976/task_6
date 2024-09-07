

from django.urls import path
from .views import *
# from .views import report_best_selling_product, report_best_seller, report_best_customer, report_sales_by_period

urlpatterns = [
    path('', index, name="index"),
    # path('customer/<int:id>/', edit_customer, name='edit_customer'),
    path('customer/<int:id>/', delete_customer, name='delete_customer'),
    path('seller/<int:id>/', delete_seller, name='delete_seller'),
    path('sale/<int:id>/', delete_sale, name='delete_sale'),
    path('product/<int:id>/', delete_product, name='delete_product'),
    path('seller_list/', seller_list, name='seller_list'),
    path('sale_list/', sale_list, name='sale_list'),
    path('product_list/', product_list, name='product_list'),
    path('customer_list/', customer_list, name='customer_list'),
    path('best-selling-product/', report_best_selling_product, name='best_selling_product'),
    path('best-seller/', report_best_seller, name='best_seller'),
    path('best-customer/', report_best_customer, name='best_customer'),
    path('sales-by-period/', report_sales_by_period, name='sales_by_period'),
    path('edit_customer/<int:id>/', edit_customer, name='edit_customer'),
    path('edit_seller/<int:id>/', edit_seller, name='edit_seller'),
    path('edit_sale/<int:id>/', edit_sale, name='edit_sale'),
    path('edit_product/<int:id>/', edit_product, name='edit_product'),
    path('report_customers_by_seller/<str:date>/', report_customers_by_seller, name='report_customers_by_seller'),
    path('report_sales_by_date/<str:date>/', report_sales_by_date, name='report_sales_by_date'),
    path('report_total_sales_by_date/<str:date>/', report_total_sales_by_date, name='report_total_sales_by_date'),
]