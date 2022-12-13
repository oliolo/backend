from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RecipeSerializer
from .models import Recipe

# Create your views here.

#class RecipeView(viewsets.ModelViewSet):
 #   serializer_class = RecipeSerializer
 #   queryset = Recipe.objects.all()
 #   lookup_field = 'slug'


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/recipe-list',
        'Detail View':'/recipe-detail/<str:pk>',
        'Create':'/recipe-create/',
		'Update':'/recipe-update/<str:pk>/',
		'Delete':'/recipe-delete/<str:pk>/',
    }

    return Response(api_urls)

@api_view(['GET'])
def recipeList(request):
    recipes = Recipe.objects.all().order_by('-id')
    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def recipeDetail(request, pk):
    recipes = Recipe.objects.get(id=pk)
    serializer = RecipeSerializer(recipes, many=False)
    return Response(serializer.data)
    
@api_view(['POST'])
def recipeCreate(request):
    serializer = RecipeSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
    
@api_view(['POST'])
def recipeUpdate(request, pk):
    recipe = Recipe.objects.get(id=pk)
    serializer = RecipeSerializer(instance=recipe, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
    
@api_view(['DELETE'])
def recipeDelete(request, pk):
    recipe = Recipe.objects.get(id=pk)
    recipe.delete()

    return Response('Item succsesfully delete!')
    