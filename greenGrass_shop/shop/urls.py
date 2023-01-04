from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('category/<category_slug>/',  views.main_catalog, name='product_list_by_category'),
    path('id=<id>/<slug>', views.product_detail, name='product_detail'),
    path('catalog/', views.main_catalog, name='main_catalog')
]