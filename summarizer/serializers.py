from rest_framework import serializers
from .models import TextSummary


class TextSummarySerializer(serializers.ModelSerializer):
    text = serializers.CharField(min_length=32, max_length=4096)
    summary = serializers.CharField(read_only=True, min_length=32)
    bullet_points = serializers.CharField(read_only=True, min_length=32)

    class Meta:
        model = TextSummary
        fields = "__all__"
        extra_kwargs = {
            "text": {"required": True},
        }
