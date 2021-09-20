from django.urls import path
from catalog.models import Category
from . import views
app_name = 'catalog'
urlpatterns = (
    path('', views.home, name='home'),
    path('category/<str:category_slug>', views.category_view, name='category_view'),
    path('product/<str:product_slug>', views.product_view, name='product_view'),
    path('product/', views.product_list_view, name='product_list_view'),


)
