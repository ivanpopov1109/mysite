from django.contrib import admin

# Register your models here.
from .models import News, Category
class NewsAdmin(admin.ModelAdmin): # создадим класс редактора, в котором можено настроить представление модели в админке
    # он должен быть подклассом редактора admin.ModelAdmin
    list_display = ('id', 'title', 'category','created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')  # чтобы в админке ссылкой был не только номер записи но еще и title
    search_fields = ('title', 'content')  # поиск в админке можео осуществлять по полям title и  content
    list_editable = ('is_published',)  # для поля опубликвано возможность редактировать прям из админки
    list_filter = ('is_published', 'category')
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)  # это кортеж!


admin.site.register(News, NewsAdmin) # здесь важен порядок разрешения моделей, сначала регистрируеся основная модель
admin.site.register(Category, CategoryAdmin)