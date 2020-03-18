from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    message = models.CharField(max_length=250)
    image = models.ImageField(
        upload_to='images/',
        height_field=None, 
        width_field=None, 
        max_length=None
        )

    def __str__(self):
        return self.title

    def summary(self):
        return self.message[:25]

    def pub_date_pretty(self):
        return self.pub_date.strftime("%b %e %Y")