from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to= '/media/')
    def __str__(self):
        return self.name
class Sizes(models.TextChoices):
    SMALL = 'S', 'Small'
    LARGE = 'L', 'Large'
    EXTRA_LARGE = 'XL', 'Extra Large'
    
class FoodItems(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, null=True, blank=True)
    size = models.CharField(max_length=10, null=True, blank=True, choices=Sizes)
    price = models.DecimalField(blank=False)
    
    
class Image(models.Model):
    name = models.CharField(primary_key=True)
    image = models.ImageField(upload_to='/media/')











