from rest_framework import serializers
from .models import SurveyPoints, SurveyLines, SurveyPolygons
from rest_framework_gis.serializers import GeoFeatureModelSerializer

# Serializer for Survey Points
class SurveyPointSerializer(GeoFeatureModelSerializer):
    """ A class to serialize Point locations as GeoJSON compatible data """

    class Meta:
        model = SurveyPoints
        geo_field = 'geom_point'
        fields = '__all__'

# Serializer for Survey Lines
class SurveyLinesSerializer(GeoFeatureModelSerializer):
    """ A class to serialize LineString locations as GeoJSON compatible data """

    class Meta:
        model = SurveyLines
        geo_field = 'geom_line'
        fields = '__all__'

# Serializer for Survey Polygons
class SurveyPolygonSerializer(GeoFeatureModelSerializer):
    """ A class to serialize Polygon locations as GeoJSON compatible data """

    class Meta:
        model = SurveyPolygons
        geo_field = 'geom_poly'
        fields = '__all__'