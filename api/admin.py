from django.contrib import admin

# Register your models here.
from api import models as api_models

admin.site.register(api_models.User)
admin.site.register(api_models.Profile)
