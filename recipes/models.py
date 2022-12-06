from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse


# Create your models here.
class Recipe(models.Model):
    portionSize = models.BigIntegerField()
    decription = models.TextField()
    creationDate = models.DateField()
    name = models.CharField(max_length=150)
    creationDate.auto_now_add = True
    slug = models.SlugField(null=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("recipe_detail", kwargs={"slug": self.slug})