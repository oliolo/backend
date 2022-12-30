from rest_framework import serializers

from .models import *

        

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description']

class CategoryListSerializer(serializers.ModelSerializer):    
    category = CategorySerializer()

    class Meta:
        model = CategoryList
        fields = ['pk', 'category']
        
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name','description']

class IngredientAmountSerializer(serializers.ModelSerializer):    
    ingredient = serializers.SerializerMethodField('get_ingredient')

    class Meta:
        model = IngredientAmount
        fields = ['pk', 'ingredient','amount']

    def get_ingredient(self, obj):
        return obj.get_ingredient(obj)

class IngredientAmountInfoSerializer(serializers.ModelSerializer):    
    ingredient = IngredientSerializer()

    class Meta:
        model = IngredientAmount
        fields = ['pk', 'ingredient','amount']


class UserSerializer(serializers.ModelSerializer):
    createdRecipes = serializers.StringRelatedField(many=True)
    savedRecipes = serializers.StringRelatedField(many=True)
    #groups = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = User
        fields = ['id', 'is_superuser', 'is_staff',  'email', 'password', 'savedRecipes', 'createdRecipes']

        
class RecipeSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    ingredients = IngredientAmountInfoSerializer(many=True, source='ingredientamount_set', read_only=True)
    author = serializers.SerializerMethodField('get_author')
    class Meta:
        model = Recipe
        fields = ['id', 'name', 'description', 'portionSize', 'creationDate', 'categories', 'ingredients', 'author', 'picture']
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


class RecipeSlugSerializer(serializers.ModelSerializer):
    recipe = RecipeSerializer()
    
    class Meta:
        model = RecipeSlug
        fields = ['recipe', 'slug']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'recipe', 'user', 'text']