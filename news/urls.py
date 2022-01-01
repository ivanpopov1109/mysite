from django.urls import path, include
# import views
from .views import *
from . import views


# Точка указывает на текущую директорию из которой из модуля views мы импортируем все функции
urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('api/', views.GetNewsAllView.as_view())
]