from django.db import models


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    images = models.TextField()
    #status 0 -> pending 1 -> available 2->  3->
    status = models.IntegerField()
    item_type = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    user_email = models.EmailField(max_length=254)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField()
    permission = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)


class Seller(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    user_email = models.EmailField(max_length=254)
    password = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    address = models.TextField()
    badge = models.CharField(max_length=255)
    is_active = models.BooleanField()
    items = models.JSONField()
    seller_type = models.CharField(max_length=255)
    permission = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
