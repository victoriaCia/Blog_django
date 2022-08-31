from django.db import models
from django.shortcuts import redirect
from django.urls import reverse

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to='blog')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'



class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'author'
        verbose_name_plural = 'authors'


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author, related_name='entries')
    image = models.ImageField(upload_to='blog/entries')
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()
    

    def __str__(self):
        return self.headline

    def get_absolute_url(self):
        return redirect(reverse("entries:entry-detail", kwargs={   
            "id": self.id
            })) 

    class Meta:
        verbose_name = 'entry'
        verbose_name_plural = 'entries'
        #order_with_respect_to = 'pub_date'
    