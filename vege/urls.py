from django.urls import path
from . import views

urlpatterns = [

    path('recipes/', views.recipes, name='recipes'),
    path('delete_recipe/<id>/', views.delete_recipe, name='delete_recipe'),
    path('update_recipe/<id>/', views.update_recipe, name='update_recipe'),
    # path('add_recipe/', views.add_recipe, name='add_recipe'),
    # path('search/', views.search, name='search'),
    # path('filter/', views.filter, name='filter'),
    # path('sort/', views.sort, name='sort'),
    # path('categories/', views.categories, name='categories'),
    # path('add_category/', views.add_category, name='add_category'),
    # path('delete_category/<id>/', views.delete_category, name='delete_category'),
    # path('update_category/<id>/', views.update_category, name='update_category'),
    # path('recipe/<id>/', views.recipe_detail, name='recipe_detail'),
    # path('category/<id>/', views.category_detail, name='category_detail'),
    # path('register/', views.register, name='register'),
    # path('login/', views.login_view, name='login'),
    # path('logout/', views.logout_view, name='logout'),
    # path('login/',views.login_page),
]