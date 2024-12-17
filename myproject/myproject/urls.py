"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import LoginClass, ViewLogin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product_list/', views.product_list, name='product_list'),
    path('', ViewLogin.as_view(), name='view_login'),
    path('login/', LoginClass.as_view(), name='login'),
    path('home/', views.ViewHome, name='view_home'),
    path('add_product/', views.product_create, name='add_product'),
    path('products/<int:pk>/update/', views.product_update, name='update_product'),  
    path('update_choose/', views.update_choose, name='update_choose'),
    path('products/<int:pk>/delete/', views.product_delete, name='delete_product'),
    path('delete_choose/', views.delete_choose, name='delete_choose'),
    path('import_list/', views.import_list, name='import_list'),
    path('export_list/', views.export_list, name='export_list'),
    path('inventory_list/', views.inventory_list, name='inventory_list'),
    path('add_import/', views.import_create, name='add_import'),
    path('add_export/', views.export_create, name='add_export'),
    path('add_inventory/', views.inventory_create, name='add_inventory'),
    path('update_choose2/', views.update_choose2, name='update_choose2'),
    path('imports/<int:pk>/update/', views.import_update, name='update_import'),
    path('update_choose3/', views.update_choose3, name='update_choose3'),
    path('exports/<int:pk>/update/', views.export_update, name='update_export'),
    path('update_choose4/', views.update_choose4, name='update_choose4'),
    path('inventory/<int:pk>/update/', views.inventory_update, name='update_inventory'),
    path('import/<int:pk>/delete/', views.import_delete, name='delete_import'),
    path('delete_choose2/', views.delete_choose2, name='delete_choose2'),
    path('export/<int:pk>/delete/', views.export_delete, name='delete_export'),
    path('delete_choose3/', views.delete_choose3, name='delete_choose3'),
    path('inventory/<int:pk>/delete/', views.inventory_delete, name='delete_inventory'),
    path('delete_choose4/', views.delete_choose4, name='delete_choose4'),
]
