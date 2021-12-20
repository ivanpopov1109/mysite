from django.db import models

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наиенование')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True) # blank=True Делает поле не обязательным
    is_published = models.BooleanField(default=True, verbose_name='Опобликовано?')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name = 'Категория' ) #воспользуемся конструктором класса ForeignKey, и напишем его во вторичной модели как обычное поле
    #Ссылку на модель можно указывать если первичная модель указана раньше, но поскольку она указана позже то мы вынуждены использовать строку с именем модели
    # models.PROTECT обеспечиввает защиту от удаления связанных данных
    verbose_name = 'Категория'
    def __str__(self): # что бы в выводе News.object.all() у нас было строковое представление названи объекта а не название приложения и его идентификатор
        return self.title

    class Meta:
        verbose_name = 'Новость'  # наименование модели в единственном числе
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']



class Category(models.Model):   # модель категорий у нас будет первичной, а модель news вторичной
        title = models.CharField(max_length=150, db_index=True, verbose_name= "Наименование категории")

        class Meta:
            verbose_name = 'Категория'  # наименование модели в единственном числе
            verbose_name_plural = 'Категории'
            ordering = ['title']

        def __str__(
                self):
            return self.title