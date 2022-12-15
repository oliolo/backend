from rest_framework import serializers

from .models import *

        

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description']
        
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name','description']
          
class UserSerializer(serializers.ModelSerializer):
    createdRecipes = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = User
        fields = ['name', 'description', 'savedRecipes', 'createdRecipes']
        
class AdminSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Admin
        fields = ['user', 'approvedRecipes']

class RecipeSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    ingredients = IngredientSerializer(many=True)
    author = serializers.StringRelatedField()
    class Meta:
        model = Recipe
        fields = ['name', 'slug', 'description', 'portionSize', 'creationDate', 'categories', 'ingredients', 'author']