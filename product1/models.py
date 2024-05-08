from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'category1'
    def __str__(self) -> str:
        return f'{self.name}'

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    model=models.CharField(max_length=100)
    price=models.IntegerField(blank=True,null=True)
    photo=models.ImageField(upload_to='media/products',blank=True,null=True)


    class Meta:
        db_table = 'product1'

        def __str__(self) -> str:
            return f'{self.category.name} {self.model}'