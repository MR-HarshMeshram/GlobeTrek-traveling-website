from django.contrib import admin

# Register your models here.
from .models import package,Destinations,Book
admin.site.register (package)
admin.site.register (Destinations)
admin.site.register (Book)
