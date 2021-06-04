from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True,
                            verbose_name='Категория')
    description = models.CharField(max_length=256, blank=True,
                                   verbose_name='Описание')
    is_active = models.BooleanField(default=True, verbose_name='активна')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name

    # def delete(self, using=None, keep_parents=False):
    #     self.is_active = False
    #     self.save(using=using)


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, verbose_name='Название продукта')
    image = models.ImageField(upload_to='products_images', blank=True)
    short_desc = models.CharField(max_length=128, blank=True,
                                  verbose_name='Краткое описание')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0,
                                           verbose_name='Количество на складе')
    is_active = models.BooleanField(default=True, verbose_name='активна')

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    def __str__(self):
        return f"{self.name} ({self.category.name})"

    @staticmethod
    def get_items():
        return Product.objects.filter(is_active=True).order_by('category', 'name')
