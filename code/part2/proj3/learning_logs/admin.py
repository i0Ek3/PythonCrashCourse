from django.contrib import admin

# Register your models here.

from leatning_logs.models import Topic # import the register model we needed

admin.site.register(Topic) # use Django manage our model by manage website
