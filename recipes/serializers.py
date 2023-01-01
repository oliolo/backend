from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from .models import *

        

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description']

class CategoryListSerializer(WritableNestedModelSerializer):    
    category = CategorySerializer()

    class Meta:
        model = CategoryList
        fields = ['pk', 'category']
        
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name','description']

class IngredientAmountSerializer(WritableNestedModelSerializer):    
    ingredient = IngredientSerializer()

    class Meta:
        model = IngredientAmount
        fields = ['pk', 'ingredient','amount']


class IngredientAmountInfoSerializer(serializers.ModelSerializer):    
    ingredient = IngredientSerializer()

    class Meta:
        model = IngredientAmount
        fields = ['pk', 'ingredient','amount']


class UserSerializer(WritableNestedModelSerializer):
    createdRecipes = serializers.StringRelatedField(many=True)
    savedRecipes = serializers.StringRelatedField(many=True)
    #groups = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = User
        fields = ['id', 'is_superuser', 'is_staff',  'email', 'password', 'savedRecipes', 'createdRecipes']

        
class RecipeSerializer(WritableNestedModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    ingredients = IngredientAmountInfoSerializer(many=True, source='ingredientamount_set', read_only=True)
    author = serializers.SerializerMethodField('get_author')
    class Meta:
        model = Recipe
        fields = ['id', 'name', 'description', 'portionSize', 'creationDate', 'categories', 'ingredients', 'author', 'picture']
        depth = 1


    def get_author(self, obj):
        return obj.get_author(obj)



class RecipeSlugSerializer(WritableNestedModelSerializer):
    recipe = RecipeSerializer()
    
    class Meta:
        model = RecipeSlug
        fields = ['recipe', 'slug']

    def create(self, validated_data):
        return RecipeSlug.objects.update_or_create(
            recipe=validated_data.pop('recipe'),
            slug=validated_data.pop('slug'),
            defaults=validated_data
        )

    def update(self, instance, validated_data):
        if 'recipe' in validated_data:
            nested_serializer = self.fields['recipe']
            nested_instance = instance.recipe
            nested_data = validated_data.pop('recipe')

            # Runs the update on whatever serializer the nested data belongs to
            nested_serializer.update(nested_instance, nested_data)

        # Runs the original parent update(), since the nested fields were
        # "popped" out of the data
        return super(UserSerializer, self).update(instance, validated_data)


class CommentSerializer(WritableNestedModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'recipe', 'user', 'text']