from django.db import models

from django.contrib import admin


# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.contrib.auth.base_user import BaseUserManager
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token



class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email=email, password=password, **extra_fields)

    def create_staff(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email=email, password=password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email=email, password=password, **extra_fields)

    


class User(AbstractUser):
    first_name = None
    last_name = None
    username = None
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    USERNAME_FIELD = 'email'
    name = models.CharField(max_length=150, null=True)
    savedRecipes = models.ManyToManyField('Recipe', blank=True)
    
    REQUIRED_FIELDS = ['password']

    objects = UserManager()

    def __str__(self):
        return self.email

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class RecipeSlug(models.Model):
    recipe = models.OneToOneField( 'Recipe',
        on_delete=models.CASCADE,
        primary_key=True,)
    slug = models.SlugField(null=False, blank=True, unique=True)


    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.recipe.name)
        return super().save(*args, **kwargs)

    
class Recipe(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    portionSize = models.BigIntegerField()
    creationDate = models.DateField()
    categories = models.ManyToManyField('Category')
    ingredients = models.ManyToManyField('Ingredient', through= 'IngredientAmount')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='createdRecipes', on_delete=models.SET_NULL, null=True)
    picture = models.FileField(upload_to='media/', null=True)
    

    def get_author(self, obj):
        return obj.author.__str__()

    def __str__(self):
        return self.name
    
    # def get_absolute_url(self):
    #     return reverse("recipe_detail", kwargs={"slug": self.slug})

    
class Ingredient(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    
    def __str__(self):
        return self.name

class IngredientAmount(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=True)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, null=True)
    amount = models.CharField(max_length=100)

    def get_recipe(self, obj):
        return obj.recipe.name

    def get_ingredient(self, obj):
        return obj.ingredient.name


    def __str__(self):
        return self.ingredient.__str__() + str(self.amount)


    
class IngredientAmountInline(admin.TabularInline):
    model = IngredientAmount
    extra = 1

class Category(models.Model):
    
    name = models.CharField(max_length=30)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
class CategoryList(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def get_recipe(self, obj):
        return obj.recipe.name

    def get_category(self, obj):
        return obj.category.name


    def __str__(self):
        return self.category.__str__()
    
class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    text = models.TextField()
    
    def __str__(self):
        return self.text
    
    