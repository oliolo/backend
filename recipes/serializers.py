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
    
    class Meta:
        model = User
        fields = ['name', 'description', 'createdRecipes', 'savedRecipes']



class RecipeSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    ingredients = serializers.StringRelatedField(many=True)
    author = serializers.StringRelatedField()
    class Meta:
        model = Recipe
        fields = ['name', 'slug', 'description', 'portionSize', 'creationDate', 'categories', 'ingredients', 'author']

class IngredientAmountSerializer(serializers.ModelSerializer):
    recipe = RecipeSerializer(many=True)
    ingredient = IngredientSerializer()

    def get_recipe(self, obj):
        return obj.recipe.name

    def get_ingredient(self, obj):
        return obj.ingredient.name

    class Meta:
        model = IngredientAmount
        fields = ['get_recipe', 'get_ingredient', 'amount']
