from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    
    def __str__(self):
        return self.first_name

    def save_editor(self):
        self.save()


    @classmethod
    def editor_profile(cls):
        profile = cls.objects.all
        return profile

class Restaurants(models.Model):
    name = models.CharField(max_length =60)
    post = models.TextField()
    editor = models.ForeignKey(Editor)
    location = models.TextField()

    

    menu_image = models.ImageField(upload_to = 'menus/')


    def __str__(self):
        return self.post

    def save_post(self):
        self.save()


    @classmethod
    def todays_menu(cls):
       
        menu = cls.objects.all
        return menu

    @classmethod
    def days_menu(cls,date):
        menu = cls.objects.all
        return menu

    @classmethod
    def search_by_name(cls,search_term):
        menu = cls.objects.filter(name__icontains=search_term)
        return menu


class Menu(models.Model):
    menu_name = models.CharField(max_length =30)
    restaurants = models.ForeignKey(Restaurants, null=True)
    price= models.CharField(max_length =30)
    


    def __str__(self):
        return self.menu_name

    def save_menu(self):
        self.save()


    @classmethod
    def editor_menu(cls):
        details = cls.objects.all
        return details


class Comment(models.Model):
    comment = models.TextField()
    resto = models.ForeignKey(Restaurants, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.comment

    
    
    
