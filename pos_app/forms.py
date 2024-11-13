from django import forms
from django.contrib.auth.models import User

from .models import Product, ProductCategory, Brand, Customer, Order, OrderItem, Payment, Inventory

# Product Form
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'barcode', 'image', 'category', 'brand', 'in_stock']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

# Product Category Form
class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['name', 'description', 'parent_category']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

# Brand Form
class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'description', 'logo']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

# Customer Form
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['user', 'name', 'email', 'phone', 'address', 'city', 'state', 'country', 'zip_code']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 2}),
        }

# Order Form
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'total_amount', 'payment_method', 'payment_status', 'status']

# Order Item Form
class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['order', 'product', 'quantity', 'price']

# Payment Form
class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['order', 'amount', 'payment_method', 'transaction_id', 'status']

# Inventory Form
class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['product', 'quantity', 'low_stock_threshold']


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label="Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_password(self):
        password = self.cleaned_data.get('password')
        return password
