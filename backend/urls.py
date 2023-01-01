"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, reverse_lazy, re_path
from django.views.generic.base import RedirectView
from rest_framework import routers
from recipes import views

router = routers.DefaultRouter()
router.register(r'recipes', views.RecipeView, 'recipe')
router.register(r'recipeSlugs', views.RecipeSlugView, 'recipe-slug')
router.register(r'users', views.UserView, 'user')
router.register(r'categories', views.CategoryView, 'category')
router.register(r'categories-list', views.CategoryListView, 'category-list')
router.register(r'ingredients', views.IngredientView, 'ingredient')
router.register(r'ingredients-amount', views.IngredientAmountView, 'ingredient-amount')
router.register(r'comments', views.CommentView, 'comment')
router.register(r'contact', views.ContactView, 'contact')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-user-login/', views.UserLogIn.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),
]
