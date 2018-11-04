from django.contrib import admin
from .models import Post, Reporter

# Register your models here.
admin.site.register(Reporter)
admin.site.register(Post)

