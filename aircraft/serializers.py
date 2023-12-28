from rest_framework import serializers
from .models import Aircraft, AircraftCharacteristic, AircraftDescription
from utils import functions


class AircraftDescriptionSerializerBase(serializers.ModelSerializer):
    class Meta:
        model = AircraftDescription
        fields = "__all__"


class AircraftDescriptionSerializer(AircraftDescriptionSerializerBase):
    class Meta(AircraftDescriptionSerializerBase.Meta):
        fields = "__all__"


class AircraftCharacteristicSerializerBase(serializers.ModelSerializer):
    class Meta:
        model = AircraftCharacteristic
        fields = "__all__"


class AircraftCharacteristicSerializer(AircraftCharacteristicSerializerBase):
    class Meta(AircraftCharacteristicSerializerBase.Meta):
        fields = "__all__"


class AircraftSerializerBase(serializers.ModelSerializer):
    description = AircraftDescriptionSerializerBase()
    characteristic = AircraftCharacteristicSerializerBase()

    class Meta:
        model = Aircraft


class AircraftReadOnlySerializer(AircraftSerializerBase):
    class Meta(AircraftSerializerBase.Meta):
        fields = "__all__"


class AircraftCreateSerializer(AircraftSerializerBase):
    class Meta(AircraftSerializerBase.Meta):
        fields = "__all__"
        read_only_fields = ["busy"]

    def create(self, validated_data):
        description_data = validated_data.pop("description")
        characteristic_data = validated_data.pop("characteristic")
        description_model = AircraftDescription.objects.create(**description_data)
        characteristic_model = AircraftCharacteristic.objects.create(
            **characteristic_data
        )
        aircraft = Aircraft.objects.create(
            **validated_data,
            description=description_model,
            characteristic=characteristic_model
        )
        return aircraft


class AircraftUpdateSerializer(AircraftSerializerBase):
    class Meta(AircraftSerializerBase.Meta):
        fields = "__all__"

    def update(self, instance, validated_data):
        functions.update_instance(instance, validated_data).save()
        functions.update_instance(
            AircraftDescription.objects.get(pk=instance.description_id),
            validated_data.pop("description", None),
        ).save()
        functions.update_instance(
            AircraftCharacteristic.objects.get(pk=instance.characteristic_id),
            validated_data.pop("characteristic", None),
        ).save()

        return instance


class AircraftDeleteSerializer(AircraftSerializerBase):
    class Meta(AircraftSerializerBase.Meta):
        fields = "__all__"
