from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    ## add 2 fields
    # Live - link to a live version available online
    # code - link to a github page with full source code

    def __str__(self):
        return self.summary
    