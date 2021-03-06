from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=2000)
    dateCreated = models.DateField(auto_now_add=True)
    url= models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.title