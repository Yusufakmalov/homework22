from django.db import models


#  models.py, admin.py, views.py, urls.py
class ProductModel(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    image = models.FileField(upload_to='products')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categoriys'



class ProductModel(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
#   category = models.ManyToManyField(CategoryModel, null = True, blank=True
    img = models.FileField(null=True, blank=True)
    description = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'products for shop'
        verbose_name_plural = 'adding products'