from rest_framework import serializers

from .models import *


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'portionSize', 'creationDate', 'slug', 'categories', 'ingredients']
        
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description']