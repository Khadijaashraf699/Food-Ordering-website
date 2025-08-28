from django.db import models
from django.utils.text import slugify

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to= 'category/')
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
            if not self.slug:  # Only generate if slug is not already set
                self.slug = slugify(self.name)
            super().save(*args, **kwargs)
    
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
    price = models.DecimalField(max_digits=5, decimal_places=5)
    
    
class Image(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='items/')











