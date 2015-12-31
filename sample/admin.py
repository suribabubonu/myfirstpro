from django.contrib import admin
from .models import newdb
# Register your models here.
from .import models
admin.site.register(models.newdb)