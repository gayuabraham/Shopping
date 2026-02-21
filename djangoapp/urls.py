from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:id>/', views.edit_product, name='edit_product'),
    path('delete/<int:id>/', views.delete_product, name='delete_product'),
    path('', views.product_list, name='product_list'),



    # API Views
    path('api/products/', views.product_api_list),
    path('api/products/create/', views.product_api_create),
    path('api/products/delete/<int:id>/', views.product_api_delete),



    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]