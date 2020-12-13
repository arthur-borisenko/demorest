from rest_framework import serializers

from clicks.models import Click


class ClickDetailSerializer(serializers.ModelSerializer):
    class Meta():
        model = Click
        fields = "__all__"
