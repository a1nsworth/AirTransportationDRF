from rest_framework import serializers

from .models import Client, ClientOrder
from utils import functions


class ClientOrderBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientOrder


class ClientOrderSerializer(ClientOrderBaseSerializer):
    class Meta(ClientOrderBaseSerializer.Meta):
        fields = "__all__"


class ClientBaseSerializer(serializers.ModelSerializer):
    order = ClientOrderSerializer()

    class Meta:
        model = Client


class ClientReadOnlySerializer(ClientBaseSerializer):
    class Meta(ClientBaseSerializer.Meta):
        fields = "__all__"


class ClientCreateSerializer(ClientBaseSerializer):
    class Meta(ClientBaseSerializer.Meta):
        fields = "__all__"
        read_only_fields = ["busy"]

    def create(self, validated_data):
        order = validated_data.pop("order")
        client_order = ClientOrder.objects.create(**order)
        client = Client.objects.create(order=client_order, **validated_data)
        return client


class ClientUpdateSerializer(ClientBaseSerializer):
    class Meta(ClientBaseSerializer.Meta):
        fields = "__all__"

    def update(self, instance, validated_data):
        functions.update_instance(
            ClientOrder.objects.get(pk=instance.order_id), validated_data.pop("order")
        ).save()
        functions.update_instance(instance, validated_data).save()

        return instance
