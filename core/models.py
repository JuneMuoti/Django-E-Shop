from django.db import models
from django.conf import settings
from django.shortcuts import reverse

# Create your models here.

CATEGORY_CHOICES=(
    ('S','Shirt'),
     ('SW','Sport wear'),
      ('OW','Out wear'),
      ('P','Phones'),
      ('E','Electronics'),
)

LABEL_CHOICES=(
    ('P','primary'),
     ('S','secondary'), 
      ('D','danger')
)

class Item(models.Model):
    title=models.CharField(max_length=100)
    price=models.FloatField()
    discount_price=models.FloatField(blank=True,null=True)
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=1 )
    label=models.CharField(choices=LABEL_CHOICES,max_length=1 ,default='P ')
    description=models.TextField()
    slug=models.SlugField()
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        
        return reverse("core:product", kwargs={'slug': self.slug})


class OrderItem(models.Model):
    item=models.ForeignKey(Item,on_delete=models.CASCADE)

class Order(models.Model):
    
    user=models.ForeignKey(settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE)
    items=models.ManyToManyField(OrderItem)   
    start_date =models.DateTimeField(auto_now_add=True) 
    ordered_date=models.DateTimeField()
    ordered=models.BooleanField(default=False)


    def __str__(self):
        return self.user.username

