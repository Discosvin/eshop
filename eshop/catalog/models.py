from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=32, verbose_name='Наименование')
    description = models.TextField(max_length=256, verbose_name='Описание')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')
    slug = models.SlugField(max_length=256, null=True, default='0')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    addon = models.ManyToManyField('Product')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=16, verbose_name='Наименование')
    description = models.TextField(max_length=256, verbose_name='Описание')
    is_vegan = models.BooleanField(verbose_name='Вегетарианская', default=False)
    slug = models.SlugField(max_length=256, null=True, default='1')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Addon(models.Model):
    name = models.CharField(max_length=32, verbose_name='Наименование')
    description = models.TextField(max_length=256, verbose_name='Описание')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')
    slug = models.SlugField(max_length=256, null=True, default='2')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Аддон'
        verbose_name_plural = 'Аддоны'

    def __str__(self):
        return self.name




