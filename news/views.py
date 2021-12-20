from django.shortcuts import render #эта функция занимается рендерингом шаблонов
from django.http import HttpResponse
from .models import News, Category # точка перед модулем указывает на текущую директорию проекта


def index(request):
    news = News.objects.order_by('-created_at') # что бы новости шли в обратном порядки создания  используем метод order_by со знаком "-"
    categories = Category.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
        'categories': categories,
    }
    return render(request, template_name='news/index.html', context=context)

def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news': news, 'categories': categories, 'category': category})
