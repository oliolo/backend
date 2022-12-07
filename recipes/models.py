from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse
from datetime import date


# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    portionSize = models.BigIntegerField()
    creationDate = models.DateField(default=date.today())
    slug = models.SlugField(null=False, unique=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("recipe_detail", kwargs={"slug": self.slug})