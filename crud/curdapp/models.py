from django.db import models

# Create your models here.
class Testbook(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.name} - {self.email}'

    