from django.contrib import admin
from .models import Restaurant, Images, Comment
# Register your models here.

admin.site.register(Restaurant)
admin.site.register(Comment)
admin.site.register(Images)