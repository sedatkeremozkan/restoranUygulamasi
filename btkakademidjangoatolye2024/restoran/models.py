from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Item(models.Model):
 
    
    user_name = models.ForeignKey(User,on_delete=models.CASCADE,default=1,related_name='kullanicilar')
    item_name = models.CharField(max_length=255)
    item_description = models.CharField(max_length=255)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500,default='')

    def __str__(self):
        return self.item_name
    

    def get_absolute_url(self):
        return reverse("restoran:detail", kwargs={"pk": self.pk})
    
class Comment(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='restoran_comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)    
    
