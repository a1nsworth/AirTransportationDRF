from rest_framework import serializers
from .models import AviationPersonnel


class AviationPersonnelSerializerBase(serializers.ModelSerializer):
    class Meta:
        model = AviationPersonnel


class AviationPersonnelReadOnlyCreateSerializer(AviationPersonnelSerializerBase):
    class Meta(AviationPersonnelSerializerBase.Meta):
        fields = "__all__"


class AviationPersonnelUpdateSerializer(AviationPersonnelSerializerBase):
    class Meta(AviationPersonnelSerializerBase.Meta):
        fields = "__all__"


class AviationPersonnelDeleteSerializer(AviationPersonnelSerializerBase):
    class Meta(AviationPersonnelSerializerBase.Meta):
        fields = "__all__"


class AviationPersonnelCreateSerializer(AviationPersonnelSerializerBase):
    class Meta(AviationPersonnelSerializerBase.Meta):
        fields = "__all__"
        read_only_fields = ["busy"]
