from rest_framework import serializers

from .models import Flight, FlightComposition
from utils import functions


class BaseFlightCompositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightComposition
        fields = "__all__"


class RepresentationFlightCompositionSerializer(BaseFlightCompositionSerializer):
    aircraft_id = serializers.StringRelatedField()
    client_id = serializers.StringRelatedField()
    pilot_main = serializers.StringRelatedField()
    pilot_assistant = serializers.StringRelatedField()
    stewards = serializers.StringRelatedField(many=True)

    class Meta(BaseFlightCompositionSerializer.Meta):
        fields = "__all__"

    def create(self, validated_data):
        raise NotImplementedError("Serializer is Representation, not implemented")

    def update(self, instance, validated_data):
        raise NotImplementedError("Serializer is Representation, not implemented")


class CreateUpdateFlightCompositionSerializer(BaseFlightCompositionSerializer):
    class Meta(BaseFlightCompositionSerializer.Meta):
        fields = "__all__"


class BaseFlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight


class RepresentationFlightSerializer(BaseFlightSerializer):
    departure_date = serializers.StringRelatedField()
    arrival_date = serializers.StringRelatedField()
    departure_city = serializers.StringRelatedField()
    arrival_city = serializers.StringRelatedField()
    composition = RepresentationFlightCompositionSerializer()

    class Meta(BaseFlightSerializer.Meta):
        fields = "__all__"

    def create(self, validated_data):
        raise NotImplementedError("Serializer is Representation, not implemented")

    def update(self, instance, validated_data):
        raise NotImplementedError("Serializer is Representation, not implemented")


class CreateCreateUpdateFlightSerializer(BaseFlightSerializer):
    composition = CreateUpdateFlightCompositionSerializer()

    class Meta(BaseFlightSerializer.Meta):
        fields = "__all__"

    def create(self, validated_data):
        composition_data = validated_data.pop("composition")
        steward_data = composition_data.pop("stewards")
        composition = FlightComposition.objects.create(**composition_data)
        for steward in steward_data:
            composition.stewards.add(steward)
        return Flight.objects.create(composition=composition, **validated_data)

    def update(self, instance, validated_data):
        composition_data = validated_data.pop("composition")
        steward_data = composition_data.pop("stewards")

        flight_composition_instance = functions.update_instance(
            FlightComposition.objects.get(pk=instance.composition_id),
            composition_data,
        )
        if len(steward_data) == 0:
            flight_composition_instance.stewards.clear()
        else:
            for steward in steward_data:
                flight_composition_instance.stewards.add(steward)

        flight_composition_instance.save()
        functions.update_instance(instance, validated_data).save()
        return instance
