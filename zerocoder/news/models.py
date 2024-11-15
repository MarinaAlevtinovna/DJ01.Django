from django.db import models
from django.contrib.auth.models import User

class NewsPost (models.Model):
    title = models.CharField('Название новости', max_length=150)
    shorts_description = models.CharField('Краткое описание новости', max_length=200)
    text = models.TextField('Новость')
    pub_date = models.DateTimeField('Дата публикации')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'