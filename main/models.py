from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя категории')
    slug = models.SlugField(max_length=255, primary_key=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    # parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:product_detail', args=[self.id, self.slug])
    # LABEL_CHOICES = (
    #     ('new', 'Новинка'),
    #     ('bestseller', 'Хит продаж'),
    #     ('ordinary', 'Обычный'),
    # )

    # class Product(models.Model):
    #     # class Meta:
    #     #     abstract = True
    #
    #     category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE, related_name='product')
    #     name = models.CharField(max_length=255, verbose_name='Наименование')
    #     slug = models.SlugField(unique=True, max_length=255)
    #     image = models.ImageField(upload_to='products', verbose_name='Изображение')
    #     description = models.TextField(verbose_name='Описание')
    #     price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    #     discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='Скидка')
    #     label = models.CharField(max_length=10, choices=LABEL_CHOICES, verbose_name='Лейбл')
    #     count_bought = models.IntegerField(verbose_name='Купили', null=True, blank=True)
    #     address = models.CharField(max_length=255, verbose_name='Адрес')


