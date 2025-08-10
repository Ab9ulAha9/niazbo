from django.db import models



class home_pics(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='niazbo_pics')

    def __str__(self):
        return self.name 
    

