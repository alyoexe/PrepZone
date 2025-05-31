from rest_framework.serializers import ModelSerializer
from base.models import Room

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'  # This will include all fields in the Room model
        # Alternatively, you can specify specific fields like this:
        # fields = ['id', 'name', 'description', 'topic']