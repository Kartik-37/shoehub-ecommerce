from django.db import models

# Create your models here.
class Category(models.Model):
     id = models.BigAutoField(primary_key=True)
     name = models.CharField(max_length=255)

     def __str__(self):
        return self.name
     
class Type(models.Model):
     id = models.BigAutoField(primary_key=True)
     name = models.CharField(max_length=255)

     def __str__(self):
        return self.name
     
class Items(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price= models.IntegerField(default=0)
    image1 = models.ImageField(null=True)
    image2 = models.ImageField(null=True)
    image3 = models.ImageField(null=True)
    image4 = models.ImageField(null=True)
    image5 = models.ImageField(null=True)
    size1 = models.IntegerField(default=0)
    size2 = models.IntegerField(default=0)
    size3 = models.IntegerField(default=0)
    size4 = models.IntegerField(default=0)
    size5 = models.IntegerField(default=0)
    width1 = models.CharField(max_length=255)
    width2 = models.CharField(max_length=255)
    width3 = models.CharField(max_length=255)
    width4 = models.CharField(max_length=255)
    description = models.TextField()
    pdetail1 = models.CharField(max_length=255)
    pdetail2 = models.CharField(max_length=255)
    pdetail3 = models.CharField(max_length=255)
    pdetail4 = models.CharField(max_length=255)
    pdetail5 = models.CharField(max_length=255)
    category = models.ManyToManyField(Category)
    type = models.ManyToManyField(Type)
    
    def __str__(self):
        return self.name

class Contact(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    message = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Cart(models.Model):
    cid = models.BigAutoField(primary_key=True)
    pid = models.IntegerField(default=0)
    username = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    price= models.IntegerField(default=0)
    image = models.ImageField(null=True)
    size1 = models.IntegerField(default=0)
    size2 = models.IntegerField(default=0)
    size3 = models.IntegerField(default=0)
    size4 = models.IntegerField(default=0)
    size5 = models.IntegerField(default=0)
    width1 = models.CharField(max_length=255)
    width2 = models.CharField(max_length=255)
    width3 = models.CharField(max_length=255)
    width4 = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class User(models.Model):
    userid = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Account(models.Model):
    aid = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    address = models.TextField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    pincode = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class Billing(models.Model):
    bid = models.BigAutoField(primary_key=True)
    oid = models.IntegerField(default=0)
    cid = models.IntegerField(default=0)
    username = models.CharField(max_length=255)
    pid = models.IntegerField(default=0)
    name = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class Payment(models.Model):
    payid = models.BigAutoField(primary_key=True)
    oid = models.IntegerField(default=0)
    username = models.CharField(max_length=255)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    address = models.TextField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    pincode = models.IntegerField(default=0)
    phone = models.CharField(max_length=255)
    cname = models.CharField(max_length=255)
    expdate = models.CharField(max_length=255)
    cvv = models.IntegerField(default=0)
    cardno = models.CharField(max_length=255)
    billing = models.ManyToManyField(Billing)

    def __str__(self):
        return self.fname

