from django.db import models

# Create your models here.
class Products(models.Model):
    def __str__(self):
        return self.title
    #title: title of item
    title = models.CharField(max_length=200)
    #item: item name for search features
    #item_search = models.CharField(max_length=200)
    #price: price of item
    price = models.DecimalField(max_digits=10, decimal_places=2)
    #category: category of item
    category = models.CharField(max_length=200)
    #color: color of item
    color = models.TextField()
    #size: size of item
    size = models.CharField(max_length=200)
    #item_detail: details of item being sold
    item_detail = models.TextField()
    #description_model: description of model measurements
    description_model = models.TextField()
    #material_made: material item is made from
    material_made = models.TextField()
    #image = models.ImageField()
    image = models.CharField(max_length=200)


class Order(models.Model):
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=500)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    address2 = models.CharField(max_length=1000)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    total = models.CharField(max_length=200)










