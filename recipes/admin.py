from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *

# Register your models here.
   
class UserAdmin(UserAdmin):
    ordering =('email',)
    list_display = ("email", "password", )
    exclude =('username', 'last_name', 'first_name')
    fieldsets = [
        ('Personal info', {'fields': ('name', 'email', 'password')}),
        ('Important dates', {'fields': ['date_joined']}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    ]

class RecipeAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "portionSize", "creationDate", "picture")
    inlines = (IngredientAmountInline,)

    #Något skapar problem här
    #def get_author(self, obj):
    #    return obj.recipe.author
    #get_author.short_description = 'Author'
    #get_author.admin_order_field = 'recipe__author'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")

class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    inlines = (IngredientAmountInline,)

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

class CategoryListAdmin(admin.ModelAdmin):
    list_display = ('get_recipe', 'get_category')
    def get_recipe(self, obj):
        return obj.recipe.name
    
    get_recipe.short_description = 'Recipe'
    get_recipe.admin_order_field = 'recipe__name'

    def get_category(self, obj):
        return obj.category.name

    get_category.short_description = 'Category'
    get_category.admin_order_field = 'category__name'


class RecipeSlugAdmin(admin.ModelAdmin):
    list_display = ('get_recipe', 'slug')

    def get_recipe(self, obj):
        return obj.recipe.name


admin.site.register(User, UserAdmin)
admin.site.register(RecipeSlug, RecipeSlugAdmin)
admin.site.register(IngredientAmount, IngredientAmountAdmin)
admin.site.register(CategoryList, CategoryListAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Comment, CommentAdmin)
