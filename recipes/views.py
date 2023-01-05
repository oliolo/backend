from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .serializers import *
from .models import *
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework import status
from rest_framework.authentication import TokenAuthentication

from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView

# Create your views here.
class RecipeSlugView(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = RecipeSlug.objects.all()
    serializer_class = RecipeSlugSerializer
    lookup_field = 'slug'

class RecipeView(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class OnlyPostOrPut(IsAuthenticated):
    
     def has_permission(self, request, view):
        if request.method in SAFE_METHODS: # GET, HEAD or OPTIONS
            return super().has_permission(request, view)
        else: # PUT, POST
            return True


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [OnlyPostOrPut]


class UserLogIn(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'id': user.pk,
            'email': user.email,
            'is_staff': user.is_staff,
            'is_superuser': user.is_superuser,
            # Including created and saved recipes produces an error
        })

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter

class CategoryView(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = Category.objects.all()
    serializer_class = CategorySerializer 

class CategoryListView(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = CategoryList.objects.all()
    serializer_class = CategoryListSerializer 

class IngredientView(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class IngredientAmountView(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = IngredientAmount.objects.all()
    serializer_class = IngredientAmountSerializer


class OnlyAutheticatedCanDelete(IsAuthenticated):
     def has_permission(self, request, view):
        if request.method == 'DELETE': 
            return super().has_permission(request, view)
        else: # PUT, POST, GET, HEAD or OPTIONS
            return True

class CommentView(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [OnlyAutheticatedCanDelete]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def destroy(self, request, *args, **kwargs):
        if request.user.is_staff:
            return super().destroy(self, request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class ContactView(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

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