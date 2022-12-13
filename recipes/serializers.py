from rest_framework import serializers

from .models import *


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'portionSize', 'slug']
        
        
class CategorySerializer(serializers.modelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description']