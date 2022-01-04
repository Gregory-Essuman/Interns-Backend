from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.SurveyPoints)
admin.site.register(models.SurveyLines)
admin.site.register(models.SurveyPolygons)