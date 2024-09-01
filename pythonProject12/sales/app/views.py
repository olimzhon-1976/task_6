from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer, Seller, Sale, Product
from .forms import CustomerForm, SellerForm, SaleForm, ProductForm
from django.db.models import Sum
from django.utils import timezone

def index(request):
    return render(request, 'app/index.html')

def edit_customer(request, id):
    customer = get_object_or_404(Customer, pk=id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'app/edit_customer.html', {'form': form})

def customer_list(request):
   query = request.GET.get('q')
   if query:
       customers = Customer.objects.filter(name__icontains=query)
   else:
       customers = Customer.objects.all()
   return render(request, 'app/customer_list.html', {'customers': customers, 'query': query})

def edit_seller(request, id):
    seller = get_object_or_404(Seller, pk=id)
    if request.method == 'POST':
        form = SellerForm(request.POST, instance=seller)
        if form.is_valid():
            form.save()
            return redirect('seller_list')
    else:
        form = SellerForm(instance=seller)
    return render(request, 'app/edit_seller.html', {'form': form})


def seller_list(request):
   query = request.GET.get('q')
   if query:
       sellers = Seller.objects.filter(name__icontains=query)
   else:
       sellers = Seller.objects.all()
   return render(request, 'app/seller_list.html', {'sellers': sellers, 'query': query})



def edit_sale(request, id):
    sale = get_object_or_404(Sale, pk=id)
    if request.method == 'POST':
        form = SaleForm(request.POST, instance=sale)
        if form.is_valid():
            form.save()
            return redirect('sale_list')
    else:
        form = SaleForm(instance=sale)
    return render(request, 'app/edit_sale.html', {'form': form})


def sale_list(request):
   query = request.GET.get('q')
   if query:
       sales = Sale.objects.filter(product__icontains=query)
   else:
       sales = Sale.objects.all()
   return render(request, 'app/sale_list.html', {'sales': sales, 'query': query})


def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'app/edit_product.html', {'form': form})

def product_list(request):
   query = request.GET.get('q')
   if query:
       products = Product.objects.filter(name__icontains=query)
   else:
       products = Product.objects.all()
   return render(request, 'app/product_list.html', {'products': products, 'query': query})

def delete_customer(request, id):
    customer = get_object_or_404(Customer, pk=id)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    return render(request, 'app/delete_confirm.html', {'object': customer})

def delete_seller(request, id):
    seller = get_object_or_404(Seller, pk=id)
    if request.method == 'POST':
        seller.delete()
        return redirect('seller_list')
    return render(request, 'app/delete_confirm.html', {'object': seller})

def delete_sale(request, id):
    sale = get_object_or_404(Sale, pk=id)
    if request.method == 'POST':
        sale.delete()
        return redirect('sale_list')
    return render(request, 'app/delete_confirm.html', {'object': sale})

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'app/delete_confirm.html', {'object': product})



def report_customers_by_seller(request, seller_id):
    query = request.GET.get('q')
    if query:
        # customers = Customer.objects.filter(sales__seller_id=query).distinct()
        customers = Customer.objects.filter(name__icontains=query)
    else:
        customers = Customer.objects.all()
    # customers = Customer.objects.filter(sales__seller_id=seller_id).distinct()
    return render(request, 'app/report_customers_by_seller.html', {'customers': customers})

def report_sales_by_date(request, date):
    sales = Sale.objects.filter(date=date)
    return render(request, 'app/report_sales_by_date.html', {'sales': sales, 'date': date})

def report_sellers_by_product(request, product_id):
    sellers = Seller.objects.filter(sales__product_id=product_id).distinct()
    return render(request, 'app/report_sellers_by_product.html', {'sellers': sellers})

def report_customers_by_product(request, product_id):
    customers = Customer.objects.filter(sales__product_id=product_id).distinct()
    return render(request, 'app/report_customers_by_product.html', {'customers': customers})

def report_total_sales_by_date(request, date):
    total_sales = Sale.objects.filter(date=date).aggregate(Sum('amount'))
    return render(request, 'app/report_total_sales_by_date.html', {'total_sales': total_sales, 'date': date})




def report_best_selling_product(request):
    product = Sale.objects.values('product__name').annotate(total_sales=Sum('amount')).order_by('-total_sales').first()
    return render(request, 'app/best_selling_product.html', {'product': product})


def report_best_seller(request):
    seller = Sale.objects.values('seller__name').annotate(total_sales=Sum('amount')).order_by('-total_sales').first()
    return render(request, 'app/best_seller.html', {'seller': seller})


def report_best_customer(request):
    customer = Sale.objects.values('customer__name').annotate(total_sales=Sum('amount')).order_by(
        '-total_sales').first()
    return render(request, 'app/best_customer.html', {'customer': customer})


def report_sales_by_period(request):
    # Получение промежутка времени из запроса
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    # Фильтрация продаж по времени
    sales = Sale.objects.filter(date__range=[start_date, end_date])

    best_selling_product = sales.values('product__name').annotate(total_sales=Sum('amount')).order_by(
        '-total_sales').first()
    best_seller = sales.values('seller__name').annotate(total_sales=Sum('amount')).order_by('-total_sales').first()
    best_customer = sales.values('customer__name').annotate(total_sales=Sum('amount')).order_by('-total_sales').first()

    context = {
        'best_selling_product': best_selling_product,
        'best_seller': best_seller,
        'best_customer': best_customer,
    }

    return render(request, 'app/sales_by_period.html', context)
