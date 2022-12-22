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
        fields = ['email', 'username', 'password', 'groups', 'savedRecipes', 'createdRecipes']



class RecipeSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    ingredients = serializers.StringRelatedField(many=True, read_only=True)
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
