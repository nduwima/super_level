from django.contrib.auth.models import User
from django.db import models



class category(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        verbose_name = 'Categorie'


    def __str__(self):
        return self.name   
             
class Commerce(models.Model):
    category = models.ForeignKey(category, on_delete=models.CASCADE) 
    name= models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='Commerce_images',blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.BooleanField(default=True)
 




  