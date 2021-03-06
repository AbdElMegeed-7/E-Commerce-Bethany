from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add_product/', views.add_product, name='add_product'),

    path('product_discerption/<int:pk>/', views.product_desc, name="product_desc"),
]
