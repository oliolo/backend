from rest_framework import serializers

from .models import *




class UserSerializer(serializer.modelSerializer):
    class Meta:
        model = User
        

class CategorySerializer(serializers.modelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description']
        
class IngredientSerializer(serializers.modelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name','description']
        
class RecipeSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    ingredients = IngredientSerializer(many=True)
    
    class Meta:
        model = Recipe
        fields = ['name', 'slug', 'description', 'portionSize', 'creationDate', 'categories', 'ingredients', 'author']