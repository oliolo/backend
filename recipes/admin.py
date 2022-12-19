from django.contrib import admin

from .models import *

# Register your models here.
   
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "name", "password")
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "portionSize", "creationDate")
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")

class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name", "description")

admin.site.register(User, UserAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Ingredient, IngredientAdmin)