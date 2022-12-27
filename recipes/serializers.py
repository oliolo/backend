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
        fields = ['is_superuser', 'is_staff',  'email', 'password', 'groups', 'savedRecipes', 'createdRecipes']


class IngredientAmountSerializer(serializers.ModelSerializer):    
    ingredient = IngredientSerializer()

    class Meta:
        model = IngredientAmount
        fields = ['pk', 'ingredient','amount']

        
class RecipeSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    ingredients = IngredientAmountSerializer(many=True, source='ingredientamount_set', read_only=True)
    author = serializers.SerializerMethodField('get_author')
    class Meta:
        model = Recipe
        fields = ['id', 'name', 'slug', 'description', 'portionSize', 'creationDate', 'categories', 'ingredients', 'author']
        depth = 1


    def get_author(self, obj):
        return obj.get_author(obj)

    def create(self, validated_data):
        recipe = Recipe.objects.create(**validated_data)
        if ('ingredients' and 'categories') in validated_data:
            ingredients_data = validated_data.pop('ingredients')
            category_data = validated_data.pop('categories')
            

            for ingredientAmount in ingredients_data:
                IngredientAmount.objects.create(recipe=recipe, **ingredientAmount)
            
            for category in category_data:
                Category.objects.create(recipe=recipe, **category)

        return recipe
