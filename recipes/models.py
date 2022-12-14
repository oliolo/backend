from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse
from datetime import date
from django.template.defaultfilters import slugify


class User(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=69)
    password = models.TextField()
    savedRecipes = models.ManyToManyField('Recipe')
    createdRecipes = models.ForeignKey("Recipe", on_delete=models.SET_NULL, null=True, related_name="+")
    
    def __str__(self):
        return self.name
    
class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    approvedRecipes = models.ManyToManyField('Recipe')
    
    def __str__(self):
        return self.user

class Recipe(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    portionSize = models.BigIntegerField()
    creationDate = models.DateField()
    slug = models.SlugField(null=False, unique=True)
    categories = models.ManyToManyField('Category')
    ingredients = models.ManyToManyField('Ingredient')
        
    
    def __str__(self):
        return self.name
    
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
    

class Category(models.Model):
    
    name = models.CharField(max_length=30)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
    
    
class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text = models.TextField()
    
    def __str__(self):
        return self.text
    
    