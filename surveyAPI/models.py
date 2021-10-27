from django.contrib.gis.db import models 
from django.contrib.auth.models import User

# Create your models here.

class SurveyPoints(models.Model):
    # Regular Django fields 
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    picture1 = models.CharField(max_length=255)
    picture2 = models.CharField(max_length=255)

    # GeoDjango-specific: a geometry field (PointField)
    geom_point = models.PointField()
    
    # Returns the string representation of the model.
    def __str__(self):
        return self.name

class SurveyLines(models.Model):
    # Regular Django fields 
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    picture1 = models.CharField(max_length=255)
    picture2 = models.CharField(max_length=255)

    # GeoDjango-specific: a geometry field (LineStringField)
    geom_line = models.LineStringField()
    
    # Returns the string representation of the model.
    def __str__(self):
        return self.name

class SurveyPolygons(models.Model):
    # Regular Django fields 
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    picture1 = models.CharField(max_length=255)
    picture2 = models.CharField(max_length=255)

    # GeoDjango-specific: a geometry field (PolygonField)
    geom_poly = models.PolygonField()
    
    # Returns the string representation of the model.
    def __str__(self):
        return self.name