from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    message = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.title