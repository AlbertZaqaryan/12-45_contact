from django.db import models

# Create your models here.


class Phone(models.Model):

    name = models.CharField('Phone name', max_length=50)
    img = models.ImageField('Phone image', upload_to='images')
    price = models.PositiveBigIntegerField('Phone price')

    def __str__(self):
        return self.name
    

class Contact(models.Model):

    user_name = models.CharField('Contact username', max_length=60)
    review = models.TextField('Contact review')

    def __str__(self):
        return self.name