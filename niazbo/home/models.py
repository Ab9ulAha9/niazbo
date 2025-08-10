from django.db import models
from cloudinary.models import CloudinaryField



class home_pics(models.Model):
    name = models.CharField(max_length=20)
    # image = models.ImageField(upload_to='niazbo_pics')
    image = CloudinaryField('image')

    def __str__(self):
        return self.name 
    

