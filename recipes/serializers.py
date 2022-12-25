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
    savedRecipes = serializers.StringRelatedField(many=True)
    groups = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = User
        fields = ['email', 'password', 'groups', 'savedRecipes', 'createdRecipes']


class IngredientAmountSerializer(serializers.ModelSerializer):    
    #ingredient = IngredientSerializer()

    class Meta:
        model = IngredientAmount
        fields = ['amount']

        
class RecipeSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    ingredients = IngredientAmountSerializer(many=True, read_only=True)
    author = UserSerializer()
    class Meta:
        model = Recipe
        fields = ['name', 'slug', 'description', 'portionSize', 'creationDate', 'categories', 'ingredients', 'author']
        depth = 1
