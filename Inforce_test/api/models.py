from django.db import models

# Create your models here.


class Menu(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=255)
    build_version = models.CharField(max_length=255)
    voted_menu = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


