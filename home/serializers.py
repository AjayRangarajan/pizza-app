from rest_framework import serializers
from .models import Topping,PizzaSize,Pizza

class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = '__all__'

class PizzaSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaSize
        fields = '__all__'

class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = '__all__'

    def to_representation(self,instance):
        representation = super().to_representation(instance)
        representation['size'] = PizzaSizeSerializer(instance.size).data
        representation['toppings'] = ToppingSerializer(instance.toppings.all(),many=True).data
        return representation