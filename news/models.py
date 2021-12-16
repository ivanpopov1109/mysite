from django.db import models

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наиенование')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True) # blank=True Делает поле не обязательным
    is_published = models.BooleanField(default=True, verbose_name='Опобликовано?')

    def __str__(self): # что бы в выводе News.object.all() у нас было строковое представление названи объекта а не название приложения и его идентификатор
        return self.title

    class Meta: #
        verbose_name = 'Новость' # наименование модели в единственном числе
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']

