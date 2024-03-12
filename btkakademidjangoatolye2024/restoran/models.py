from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Item(models.Model):
 
    
    user_name = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    item_name = models.CharField(max_length=255)
    item_description = models.CharField(max_length=255)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500,default='https://livingstonbagel.com/wp-content/uploads/2016/11/food-placeholder.jpg')

    def __str__(self):
        return self.item_name
    

    def get_absolute_url(self):
        return reverse("restoran:detail", kwargs={"pk": self.pk})
    
class Comment(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)    
    
