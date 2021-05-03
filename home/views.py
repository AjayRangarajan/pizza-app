from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Topping, PizzaSize, Pizza
from .serializers import ToppingSerializer, PizzaSizeSerializer, PizzaSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def home(request):
    api_urls = {
        'Home': '',
        'Pizza List': '/pizza-list/',
        'Pizza Detail': '/pizza-detail/<int:pk>/',
        'Create Pizza': '/create-pizza/',
        'Update Pizza': '/update-pizza/<int:pk>/',
        'Delete Pizza': '/delete-pizza/<int:pk>/',
        'Pizza Size List': '/pizza-size-list/',
        'Create Pizza Size': '/create-pizza-size/',
        'Toppings List': '/toppings-list/',
        'Create Topping': '/create-topping/',
    }
    return Response(api_urls)
    # return render(request,template_name="home/home.html")

@api_view(['GET'])
def pizzaList(request):
    pizzas = Pizza.objects.all()
    serializer = PizzaSerializer(pizzas, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def pizzaDetail(request, pk):
    pizza = Pizza.objects.get(id=pk)
    serializer = PizzaSerializer(pizza, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createPizza(request):
    serializer = PizzaSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def updatePizza(request, pk):
    pizza = Pizza.objects.get(id=pk)
    serializer = PizzaSerializer(instance=pizza, data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deletePizza(request, pk):
    pizza = Pizza.objects.get(id=pk)
    pizza.delete()
    return Response('Successfully deleted pizza!!!')

@api_view(['GET'])
def pizzaSizeList(request):
    pizzaSizes = PizzaSize.objects.all()
    serializer = PizzaSizeSerializer(pizzaSizes, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createPizzaSize(request):
    serializer = PizzaSizeSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def toppingsList(request):
    toppings = Topping.objects.all()
    serializer = ToppingSerializer(toppings, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createTopping(request):
    serializer = ToppingSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()

    return Response(serializer.data)
