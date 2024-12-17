from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate, login, decorators
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

# Create your views here.
from django.shortcuts import render, redirect
from .models import Product, Import, Export, Inventory
from .forms import ProductForm, ImportForm, ExportForm, InventoryForm  # Assuming you have forms defined
from django.http import HttpResponse

def product_list(request):
    products = Product.objects.all()
    context = {'products': products} 
    return render(request, 'product_list.html', context)

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

def product_update(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return render(request,'product_list.html')
    else:
        form = ProductForm(instance=product)
    return render(request, 'update_product.html', {'form': form})

def product_delete(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return redirect('view_home')

def import_list(request):
    imports = Import.objects.all()
    return render(request, 'import_list.html', {'imports': imports})

def import_create(request):
    if request.method == 'POST':
        form = ImportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('import_list')
    else:
        form = ImportForm()
    return render(request, 'add_import.html', {'form': form})

def import_update(request, pk):
    import_item = Import.objects.get(pk=pk)
    if request.method == 'POST':
        form = ImportForm(request.POST, instance=import_item)
        if form.is_valid():
            form.save()
            return redirect('import_list')
    else:
        form = ImportForm(instance=import_item)
    return render(request, 'update_import.html', {'form': form})

def import_delete(request, pk):
    import_item = Import.objects.get(pk=pk)
    import_item.delete()
    return redirect('import_list')

def export_list(request):
    exports = Export.objects.all()
    return render(request, 'export_list.html', {'exports': exports})

def export_create(request):
    if request.method == 'POST':
        form = ExportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('export_list')
    else:
        form = ExportForm()
    return render(request, 'add_export.html', {'form': form})

def export_update(request, pk):
    export_item = Export.objects.get(pk=pk)
    if request.method == 'POST':
        form = ExportForm(request.POST, instance=export_item)
        if form.is_valid():
            form.save()
            return redirect('export_list')
    else:
        form = ExportForm(instance=export_item)
    return render(request, 'update_export.html', {'form': form})

def export_delete(request, pk):
    export_item = Export.objects.get(pk=pk)
    export_item.delete()
    return redirect('export_list')

def inventory_list(request):
    inventory = Inventory.objects.all()
    return render(request, 'inventory_list.html', {'inventory': inventory})

def inventory_create(request):
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory_list')
    else:
        form = InventoryForm()
    return render(request, 'add_inventory.html', {'form': form})

def inventory_update(request, pk):
    inventory = Inventory.objects.get(pk=pk)
    if request.method == 'POST':
        form = InventoryForm(request.POST, instance=inventory)
        if form.is_valid():
            form.save()
            return redirect('inventory_list')
    else:
        form = InventoryForm(instance=inventory)
    return render(request, 'update_inventory.html', {'form': form})

def inventory_delete(request, pk):
    inventory = Inventory.objects.get(pk=pk)
    inventory.delete()
    return redirect('inventory_list')

class LoginClass(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        user_name = request.POST.get('user')
        password = request.POST.get('password')
        my_user = authenticate(username = user_name,password = password)
        if my_user is None:
            return HttpResponse('Đăng nhập thất bại')

        login(request, my_user)
        return render(request, 'home.html')

class ViewLogin(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        return render(request, 'home.html')

    def post(self, request):
        pass

@decorators.login_required(login_url='/login/')
def ViewHome(request):
    return render(request, 'home.html')

def update_choose(request):
    products = Product.objects.all()
    context = {'products': products} 
    return render(request, 'update_choose.html', context)

def delete_choose(request):
    products = Product.objects.all()
    context = {'products': products} 
    return render(request, 'delete_choose.html', context)

def update_choose2(request):
    products = Import.objects.all()
    context = {'products': products} 
    return render(request, 'update_choose2.html', context)

def update_choose3(request):
    products = Export.objects.all()
    context = {'products': products} 
    return render(request, 'update_choose3.html', context)

def update_choose4(request):
    products = Inventory.objects.all()
    context = {'products': products} 
    return render(request, 'update_choose4.html', context)

def delete_choose2(request):
    products = Import.objects.all()
    context = {'products': products} 
    return render(request, 'delete_choose2.html', context)

def delete_choose3(request):
    products = Export.objects.all()
    context = {'products': products} 
    return render(request, 'delete_choose3.html', context)

def delete_choose4(request):
    products = Inventory.objects.all()
    context = {'products': products} 
    return render(request, 'delete_choose4.html', context)