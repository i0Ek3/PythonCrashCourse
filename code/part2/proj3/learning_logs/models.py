from django.db import models

# Create your models here.

class Topic(models.Model):
    """The topic of user learning"""

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self): #If you use python2.7 please change this function into __unicode__()
        """Return the string of model"""

        return self.text
