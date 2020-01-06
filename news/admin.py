from django.contrib import admin
from .models import NewCategory,News
# Register your models here.
admin.site.register([NewCategory,News])
