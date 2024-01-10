from rest_framework import serializers
from .models import job_details
class jobserializers(serializers.ModelSerializer):
    class Meta:
        model = job_details
        fields = "__all__"