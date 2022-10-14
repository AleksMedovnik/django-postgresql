from django.db import models

class User(models.Model):
   name = models.CharField(max_length=150, db_index=True)
   age = models.IntegerField()

   def __str__(self):
       return self.name


class Post(models.Model):
   title = models.CharField(max_length=150)
   content = models.TextField()

   def __str__(self):
       return self.title