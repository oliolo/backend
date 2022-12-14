from rest_framework import serializers

from .models import *

        

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
        
class UserSerializer(serializers.modelSerializer):
    createdRecipes = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = User
        fields = ['name', 'description', 'savedRecipes', 'createdRecipes']
        
class AdminSerializer(serializers.modelSerializer):
    
    class Meta:
        model = Admin
        fields = ['user', 'approvedRecipes']