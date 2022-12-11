from django.shortcuts import render
from rest_framework import serializers, viewsets

from api.models import VoterRecord
from api.serializers import VoterRecordSerializer


# ViewSets define the view behavior.
class VoterRecordViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = VoterRecord.objects.all()
    serializer_class = VoterRecordSerializer

# Routers provide an easy way of automatically determining the URL conf.
