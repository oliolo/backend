from django.contrib import admin

from .models import *

# Register your models here.
   
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "name", "password")

class RecipeAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "portionSize", "creationDate", 'get_author')

    def get_author(self, obj):
        return obj.recipe.author
    get_author.short_description = 'Author'
    get_author.admin_order_field = 'recipe__author'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")

class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name", "description")

class CommentAdmin(admin.ModelAdmin):
    pass

class IngredientAmountAdmin(admin.ModelAdmin):
    list_display = ('get_recipe', 'get_ingredient', 'amount')
    def get_recipe(self, obj):
        return obj.recipe.name
    
    get_recipe.short_description = 'Recipe'
    get_recipe.admin_order_field = 'recipe__name'

    def get_ingredient(self, obj):
        return obj.ingredient.name

    get_ingredient.short_description = 'Ingredient'
    get_ingredient.admin_order_field = 'ingredient__name'

    

admin.site.register(User, UserAdmin)
admin.site.register(IngredientAmount, IngredientAmountAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Comment, CommentAdmin)