from django.shortcuts import render, redirect
from django.http import JsonResponse

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *

# Create your views here.
class RecipeView(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    lookup_field = 'slug'

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer 

class IngredientView(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class IngredientAmountView(viewsets.ModelViewSet):
    queryset = IngredientAmount.objects.all()
    serializer_class = IngredientAmountSerializer

"""
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
    


    # Create your views here.  
def emp(request):  
    if request.method == "POST":  
        form = RecipeSerializer(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = RecipeSerializer()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    employees = Recipe.objects.all()  
    return render(request,"show.html",{'employees':employees})  
def edit(request, id):  
    employee = Recipe.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  
def update(request, id):  
    employee = Recipe.objects.get(id=id)  
    form = RecipeSerializer(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})  
def destroy(request, id):  
    employee = Recipe.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")  
    """