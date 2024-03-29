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
        fields = ['id', 'category']
        
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name','description']

class IngredientAmountSerializer(WritableNestedModelSerializer):    

    class Meta:
        model = IngredientAmount
        fields = ['id', 'recipe', 'ingredient','amount']


    

class IngredientAmountInfoSerializer(serializers.ModelSerializer):    
    ingredient = IngredientSerializer()

    class Meta:
        model = IngredientAmount
        fields = ['id', 'ingredient','amount']


class UserSerializer(WritableNestedModelSerializer):
    createdRecipes = serializers.StringRelatedField(many=True, read_only=True)
    savedRecipes = serializers.StringRelatedField(many=True, read_only=True)
    #groups = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = User
        fields = ['id', 'is_superuser', 'is_staff',  'email', 'password', 'savedRecipes', 'createdRecipes']
        
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user
    
    def update(self, instance, validated_data):
        password = validated_data.get('password', instance.password)
        
        instance = super().update(instance, validated_data)
        instance.set_password(password)
        instance.save()
        return instance

        
class RecipeSerializer(WritableNestedModelSerializer):
    categories = CategorySerializer(many=True, read_only=False, required = False)
    ingredients = IngredientAmountInfoSerializer(many=True, source='ingredientamount_set', read_only=False, required = False)
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

    # def create(self, validated_data):
    #     return RecipeSlug.objects.update_or_create(
    #         recipe=validated_data.pop('recipe'),
    #         slug=validated_data.pop('slug'),
    #         defaults=validated_data
    #     )

    def update(self, instance, validated_data):
        if 'recipe' in validated_data:
            nested_serializer = self.fields['recipe']
            nested_instance = instance.recipe
            nested_data = validated_data.pop('recipe')

            # Runs the update on whatever serializer the nested data belongs to
            nested_serializer.update(nested_instance, nested_data)

        # Runs the original parent update(), since the nested fields were
        # "popped" out of the data
        return super(RecipeSlugSerializer, self).update(instance, validated_data)


class CommentSerializer(WritableNestedModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'recipe', 'user', 'text']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'full_name', 'email', 'query']