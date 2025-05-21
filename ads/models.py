from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ad(models.Model):

    title = models.CharField(max_length=256)
    description = models.TextField(max_length=2048)
    image = models.ImageField(upload_to='ads_images', verbose_name='image')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(to='accounts.User', on_delete=models.CASCADE, related_name='ads')

    def __str__(self):
        return f'{self.title} - {self.price}'
