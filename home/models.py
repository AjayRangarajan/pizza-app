from django.db import models


class Topping(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class PizzaSize(models.Model):
    size = models.CharField(max_length=50)

    def __str__(self):
        return self.size
    

class Pizza(models.Model):
    default_pizza_type = "Regular"
    pizza_types= (
        (u'regular',"Regular"),
        (u'square',"Square"),
    )
    type = models.CharField(verbose_name="type",choices=pizza_types,max_length=50,blank=False,default=default_pizza_type)

    default_pizza_size = "medium"
    size = models.ForeignKey("PizzaSize", verbose_name="size", on_delete=models.CASCADE,blank=False,default=default_pizza_size)

    toppings = models.ManyToManyField("Topping", verbose_name= "toppings",related_name="pizza")

    def __str__(self):
        return f'{self.type}-{self.size} Pizza'

    def create(self,validated_data):
        return Pizza.objects.create(**validated_data)