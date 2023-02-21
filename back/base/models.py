from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    user =models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    desc = models.CharField(max_length=50,null=True,blank=True)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    createdTime=models.DateTimeField(auto_now_add=True)
    fields =['desc','price']
 
    def __str__(self):
           return self.desc
########## clients ##########
class Client(models.Model):
    id = models.BigAutoField(primary_key=True)
    cName = models.CharField(max_length=20)
    age = models.FloatField()



    def __str__(self):
        return self.cName
########## clients ##########

class Product(models.Model):
    user =models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

##### image #####
class Task(models.Model):
    user =models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    image = models.ImageField(null=True,blank=True,default='/placeholder.png')
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
   
    def __str__(self):
        return self.title
##### image #####

