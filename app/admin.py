from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(SmokeData)
admin.site.register(HumanData)
admin.site.register(ObjectData)