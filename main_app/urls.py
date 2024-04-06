from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('plantains/', views.plantains_index, name='index'),
    path('plantains/<int:plantain_id>/', views.plantains_detail, name='detail'),
    path('plantains/create', views.PlantainCreate.as_view(), name='plantains_create'),
    path('plantains/<int:pk>/update/', views.PlantainUpdate.as_view(), name='plantains_update'),
    path('plantains/<int:pk>/delete/', views.PlantainDelete.as_view(), name='plantains_delete'),
    path('plantains/<int:plantain_id>/add_recipe/', views.add_recipe, name='add_recipe'),
    # Associations of Plantain and Drink
     path('plantains/<int:plantain_id>/assoc_drink/<int:drink_id>/', views.assoc_drink, name='assoc_drink'),
     path('plantains/<int:plantain_id>/unassoc_drink/<int:drink_id>/', views.unassoc_drink, name='unassoc_drink'),
    # Drinks
    path('drinks/', views.DrinkList.as_view(), name='drinks_index'),
    path('drinks/<int:pk>/', views.DrinkDetail.as_view(), name='drinks_detail'),
    path('drinks/create/', views.DrinkCreate.as_view(), name='drinks_create'),
    path('drinks/<int:pk>/update/', views.DrinkUpdate.as_view(), name='drinks_update'),
    path('drinks/<int:pk>/delete/', views.DrinkDelete.as_view(), name='drinks_delete'),

]
