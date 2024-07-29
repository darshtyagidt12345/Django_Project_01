from django.db import models

# Create your models here.
class Contact(models.Model):
   name = models.CharField(max_length=130)
   email = models.EmailField()
   phone = models.CharField(max_length=12)
   desc = models.TextField()
   age = models.IntegerField(default=0)
   date = models.DateField()
   def __str__(self):
      return f"{self.name} "
class Blog(models.Model):
   title = models.CharField(max_length=50)
   content = models.TextField()
   user = models.CharField(max_length=1000000000)
   def __str__(self):
       return f"{self.user}, {self.title}"
   