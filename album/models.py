from django.db import models
import datetime as dt

class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)

    def __str__(self):
        return self.first_name

    def save_editor(self):
        self.save()

class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length =60)
    post = models.TextField()
    editor = models.ForeignKey(Editor)
    tags = models.ManyToManyField(tags)
    category = models.ForeignKey(Category, null=True)
    location = models.ForeignKey(Location, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def todays_album(cls):
        today = dt.date.today()
        album = cls.objects.filter(pub_date__date = today)
        return album

    @classmethod
    def days_album(cls,date):
        album = cls.objects.filter(pub_date__date = date)
        return album

    @classmethod
    def search_by_title(cls,search_term):
        album = cls.objects.filter(title__icontains=search_term)
        return album