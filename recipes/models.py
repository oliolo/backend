from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify


class User(AbstractUser):
    first_name = None
    last_name = None
    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = email
    name = models.CharField(max_length=150, null=True)
    savedRecipes = models.ManyToManyField('Recipe')
    
    REQUIRED_FIELDS = []
    #savedRecipes = models.ManyToManyField('Recipe')   
    def __str__(self):
        return self.username
    
# class Admin(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     approvedRecipes = models.ManyToManyField('Recipe')
    
#     def __str__(self):
#         return self.user

class Recipe(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(null=False, unique=True)
    description = models.TextField()
    portionSize = models.BigIntegerField()
    creationDate = models.DateField()
    categories = models.ManyToManyField('Category')
    ingredients = models.ManyToManyField('Ingredient', through= 'IngredientAmount', through_fields=('recipe', 'ingredient'))
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='createdRecipes', on_delete=models.SET_NULL, null=True)
        
    
    def __str__(self):
        return "PK: " + str(self.pk) + "   " + self.name
    
    def get_absolute_url(self):
        return reverse("recipe_detail", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    
class Ingredient(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    
    def __str__(self):
        return self.name

class IngredientAmount(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=True)
    ingredient = models.ForeignKey(Ingredient,  on_delete=models.CASCADE, null=True)
    amount = models.BigIntegerField()

    def __str__(self):
        return self.ingredient.__str__ + str(self.amount)


    

class Category(models.Model):
    
    name = models.CharField(max_length=30)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
    
    
class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    text = models.TextField()
    
    def __str__(self):
        return self.text
    
    