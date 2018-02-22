from django.db import models

# Create your models here.

class Topic(models.Model):
    """The topic of user learning"""

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self): #If you use python2.7 please change this function into __unicode__()
        """Return the string of model"""

        return self.text

class Entry(models.Model):
    """Specific knowlage of learned about topics"""
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

        def __str__(self): #python2.7 please use __unicode__()
            """return string of model"""
            return self.text[:50] + "..."
