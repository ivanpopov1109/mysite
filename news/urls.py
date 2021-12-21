from django.urls import path
from .views import *
# Точка указывает на текущую директорию из которой из модуля views мы импортируем все функции
urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>/', get_category, name='category')

]