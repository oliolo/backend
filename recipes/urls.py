from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('recipe-list/', views.recipeList, name="recipe-list"),
	path('recipe-detail/<str:pk>/', views.recipeDetail, name="recipe-detail"),
	path('recipe-create/', views.recipeCreate, name="recipe-create"),

	path('recipe-update/<str:pk>/', views.recipeUpdate, name="recipe-update"),
	path('recipe-delete/<str:pk>/', views.recipeDelete, name="recipe-delete"),
]