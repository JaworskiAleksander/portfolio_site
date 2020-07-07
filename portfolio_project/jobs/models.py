from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    ## add 2 fields
    # Live - link to a live version available online
    live_app_link = models.URLField(null=True, blank=True, default='', max_length=250)
    # code - link to a github page with full source code
    code_source_link = models.URLField(null=True, blank=True, default='', max_length=250)

    def __str__(self):
        return self.summary
    
    def short(self):
        return self.summary + "testing"