from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


class Post(models.Model):
        sno = models.AutoField(primary_key=True)
        title = models.CharField(max_length=255)
        content = RichTextField(blank=True, null=True)
        author = models.CharField(max_length=255)
        slug = models.CharField(max_length=200)
        timeStamp = models.DateTimeField(blank=True)
       
        
        def __str__(self):
                return 'Message from ' +self.title + ' by ' + self.author
        
        def get_absolute_url(self):
                return reverse('home')

class News(models.Model):
        sno = models.AutoField(primary_key=True)
        title = models.CharField(max_length=255)
        content = RichTextField(blank=True, null=True)
        author = models.CharField(max_length=255)
        slug = models.CharField(max_length=200)
        timeStamp = models.DateTimeField(blank=True)
        image = models.ImageField(upload_to="images/")

        def __str__(self):
                return 'News from ' +self.title + ' by ' + self.author


class Contact(models.Model):
        sno = models.AutoField(primary_key=True)
        name = models.CharField(max_length=255)
        phone = models.CharField(max_length=12)
        email = models.CharField(max_length=255)
        comment = models.CharField(max_length=255)
        
        def __str__(self):
                return 'Feedback from ' +self.name 

        