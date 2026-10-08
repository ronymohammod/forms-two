from django.shortcuts import render,redirect,get_object_or_404
from form_app.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm


def register_view(request):
    form_data=RegisterForm()
    if request.method=="POST":
        form_data=RegisterForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('login_view')

    context={
        'form_data':form_data
    }

    return render(request,'register.html',context)

def login_view(request):
    form_data=AuthenticationForm()
    if request.method=="POST":
        form_data=AuthenticationForm(request,data=request.POST)
        if form_data.is_valid():
            user=form_data.get_user()
            if user:
                login(request,user)
                return redirect('dashboard_view')
    context={
        'form_data':form_data

    }        
    return render(request, 'login.html',context)

@login_required
def dashboard_view(request):
    return render(request,'dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login_view')

def category_list(request):
    category_data=CategoryModel.objects.all()
    context={
        'category_data':category_data
    }
    return render(request,'category-list.html',context)


def add_category(request):
    form_data=CategoryForm()
    if request.method == "POST":
        form_data=CategoryForm(request.POST)

        if form_data.is_valid():
                form_data.save()
                return redirect('category_list')
    context={
         'form_data':form_data
         
    }
    return render(request,'add-category.html',context)

def update_category(request,id):
    categoty_data=get_object_or_404(CategoryModel,id=id)
    form_data = CategoryForm(instance=categoty_data)

    if request.method=="POST":
        form_data=CategoryForm(request.POST,instance=categoty_data)
        if form_data.is_valid():
            form_data.save()
            return redirect('category_list')
        
    context={
        'form_data':form_data
    } 
    return render(request,'update-categoty.html',context)  

def delete_category(request,id):
     get_object_or_404(CategoryModel,id=id).delete()
     return redirect('category_list')



def add_product(request):
    form_data=ProductForm()
    if request.method=="POST":
        form_data=ProductForm(request.POST)
        if form_data.is_valid():
            data=form_data.save(commit=False)
            data.created_by=request.user
            data.total_amount=data.price * data.qty
            data.save()
            return redirect('product_list')
    context={
        'form_data':form_data
    }
    return render(request,'add-product.html',context)


def product_list(request):
    product_data=ProductModel.objects.all()
    context={
            'product_data':product_data
    }
    return render(request,'product-list.html',context)


def edit_product(request,p_id):
    product_data=get_object_or_404(ProductModel,id=p_id)
    form_data=ProductForm(instance=product_data)
    if request.method=="POST":
        form_data=ProductForm(request.POST,instance=product_data)
        if form_data.is_valid():
            data=form_data.save(commit=False)
            data.total_amount=data.price * data.qty
            data.save()
            return redirect('product_list')

    context={
        'form_data':form_data
    }
    return render(request,'edit-product.html',context)

def delete_product(request,p_id):
    get_object_or_404(ProductModel,id=p_id).delete()
    return redirect('product_list')



          
               
          

          

                

