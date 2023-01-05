from rest_framework import serializers

from api.models import VoterRecord


class VoterRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoterRecord
        fields = ['identity_number', 'block_code', 'polling_station','serial_number']
