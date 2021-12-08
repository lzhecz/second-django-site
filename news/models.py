from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length = 150, verbose_name = 'Название новости', db_index = True)
    slug = models.SlugField(blank = True)
    content = models.TextField(blank = True, verbose_name = 'Текст статьи')
    photo = models.ImageField(blank = True, upload_to = "photos/%Y/%m/%d/", verbose_name = 'Фото')
    time_create = models.DateTimeField(auto_now_add = True, verbose_name = 'Время создания')
    time_update = models.DateTimeField(auto_now = True, verbose_name = 'Время обновления')
    is_published = models.BooleanField(default = True, verbose_name = 'Публикация')
    category = models.ForeignKey('Category', on_delete = models.PROTECT, verbose_name = 'Категория')

    def get_absolute_url(self):
        return reverse('view_news', kwargs = {'pk': self.pk})

    def __str__(self):
        return f'[{self.pk}] {self.title}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-time_create']


class Category(models.Model):
    title = models.CharField(max_length = 150, verbose_name = 'Название категории', db_index = True)
    slug = models.SlugField(blank = True)

    def get_absolute_url(self):
        return reverse('category', kwargs = {'category_id': self.pk})

    def __str__(self):
        return f'[{self.pk}] {self.title}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
