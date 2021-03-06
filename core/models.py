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
    def get_add_to_cart_url(self):
        return reverse("core:add_to_cart", kwargs={'slug': self.slug})
    def get_remove_from_cart_url(self):
        return reverse("core:remove_from_cart", kwargs={'slug': self.slug})
        

class OrderItem(models.Model):
    item=models.ForeignKey(Item,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE)
    ordered=models.BooleanField(default=False)

    def  __str__(self):
        return "{} of {}.".format(self.quantity,self.item.title)
    def get_total_item_price(self):
        return self.quantity*self.item.price
    def get_total_item_discount_price(self):
        return self.quantity*self.item.discount_price
    def get_amount_saved(self):
        return (self.item.price-self.item.discount_price)*self.quantity
    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_item_discount_price()
        return self.get_total_item_price()
class Order(models.Model):
    
    user=models.ForeignKey(settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE)
    items=models.ManyToManyField(OrderItem)   
    start_date =models.DateTimeField(auto_now_add=True) 
    ordered_date=models.DateTimeField()
    ordered=models.BooleanField(default=False)


    def __str__(self):
        return self.user.username

    def get_total_price(self):
        total=0
        for order_item in self.items.all():
            total+= order_item.get_final_price()
        return total



