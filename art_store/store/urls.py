from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # URL for the index page
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),  # URL for product detail page
]
