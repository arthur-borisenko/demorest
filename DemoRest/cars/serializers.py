from rest_framework import serializers

from cars.models import Car


class CarListSerializer(serializers.ModelSerializer):
    class Meta():
        model = Car
        fields = ("id", 'vin', 'Users',)


class CarDetailSerializer(serializers.ModelSerializer):
    Users = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta():

        model = Car
        fields = "__all__"
