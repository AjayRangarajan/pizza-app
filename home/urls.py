from django.urls import path, include
from . import views as home_views

app_name = "home"

urlpatterns = [
    path('', home_views.home, name="home"),
    path('pizza-list/', home_views.pizzaList, name="pizza_list"),
    path('pizza-detail/<int:pk>/', home_views.pizzaDetail, name="pizza_detail"),
    path('create-pizza/', home_views.createPizza, name="create_pizza"),
    path('update-pizza/<int:pk>/', home_views.updatePizza, name="update_pizza"),
    path('delete-pizza/<int:pk>/', home_views.deletePizza, name="delete_pizza"),
    path('pizza-size-list/',home_views.pizzaSizeList, name="pizza_size_list"),
    path('create-pizza-size/',home_views.createPizzaSize, name="create_pizza_size"),
    path('toppings-list/',home_views.toppingsList, name="toppings_list"),
    path('create-topping/',home_views.createTopping, name="create_topping"),
]
