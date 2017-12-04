from django.contrib import admin

# Register your models here.

from learning_logs.models import Topic # import the register model we needed

admin.site.register(Topic) # use Django manage our model by manage website
admin.site.register(Entry)

