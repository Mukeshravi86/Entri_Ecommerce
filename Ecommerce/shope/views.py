from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User





@login_required
def home(request):
    return render(request,'home.html')

@login_required
def login_view(request):
    if request.method=='POST':

      uname=request.POST('username')
      pwd=request.POST('password')
      user=authenticate(request,username=uname,password=pwd)
      if user is not None:
        login(request,user)
        return redirect('product_details')
      else:
        return render(request,'login.html',{'msg':'invalid details'})
    else:
        return render(request,'login.html')
    
def logout_view(request):
    logout(request)
    return redirect('login.html')     
    
def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
          User=form.save()
          return redirect('login')
        return render(request,'register.html',{'form':form,'msg':'inavlid details'})
    else:
        form=UserCreationForm()
        return render(request,'register.html',{'form':form,'msg':'invalid details'})
    



def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def product_details(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_details.html', {'product': product})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})


def edit_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit_product.html', {'form': form})


def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'delete_product.html', {'product': product})


