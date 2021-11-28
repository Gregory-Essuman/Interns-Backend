from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from surveyapi.models import SurveyPoints, SurveyLines, SurveyPolygons
from .serializers import SurveyPointSerializer, SurveyLinesSerializer, SurveyPolygonSerializer

class PointApiViewset(viewsets.ModelViewSet):
    serializer_class = SurveyPointSerializer
    queryset = SurveyPoints.objects.all()

class LineApiViewset(viewsets.ModelViewSet):
    serializer_class = SurveyLinesSerializer
    queryset = SurveyLines.objects.all()

class PolygonApiViewset(viewsets.ModelViewSet):
    serializer_class = SurveyPolygonSerializer
    queryset = SurveyPolygons.objects.all()