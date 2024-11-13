from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, ProductCategory, Brand, Order, OrderItem, Customer
from .forms import ProductForm, OrderForm, OrderItemForm, CustomerForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate, login ,logout

# Product Views
def product_list(request):
    products = Product.objects.all()
    return render(request, 'pos/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'pos/product_detail.html', {'product': product})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm()
    return render(request, 'pos/product_form.html', {'form': form})

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'pos/product_form.html', {'form': form})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'pos/product_confirm_delete.html', {'product': product})

# Order Views
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'pos/order_list.html', {'orders': orders})

def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'pos/order_detail.html', {'order': order})

def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            return redirect('order_detail', pk=order.pk)
    else:
        form = OrderForm()
    return render(request, 'pos/order_form.html', {'form': form})

def order_update(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_detail', pk=order.pk)
    else:
        form = OrderForm(instance=order)
    return render(request, 'pos/order_form.html', {'form': form})

def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')
    return render(request, 'pos/order_confirm_delete.html', {'order': order})

# Customer Views
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'pos/customer_list.html', {'customers': customers})

def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'pos/customer_detail.html', {'customer': customer})

def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            return redirect('customer_detail', pk=customer.pk)
    else:
        form = CustomerForm()
    return render(request, 'pos/customer_form.html', {'form': form})

def customer_update(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_detail', pk=customer.pk)
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'pos/customer_form.html', {'form': form})

def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    return render(request, 'pos/customer_confirm_delete.html', {'customer': customer})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Create user without password validation constraints
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Save the password securely
            user.save()
            messages.success(request, 'Your account has been created! You can now log in.')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request, 'auth/register.html', {'form': form})



def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # If authentication is successful, log the user in
            login(request, user)
            messages.success(request, 'You have successfully logged in!')
            return redirect('home')  # Redirect to the home page or any other page
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'auth/login.html')


def custom_logout(request):
    logout(request)  # Log out the user
    return redirect('login')  # Redirect to the home page or any other page after logout


def homepage(request):
    # Fetch the latest products and orders
    featured_products = Product.objects.all()[:6]  # Get 6 featured products
    recent_orders = Order.objects.all().order_by('-order_date')[:5]  # Get 5 most recent orders
    customers = Customer.objects.all().order_by('-created_at')[:5]  # Get 5 most recent customers

    context = {
        'featured_products': featured_products,
        'recent_orders': recent_orders,
        'customers': customers,
    }
    return render(request, 'pos/homepage.html', context)