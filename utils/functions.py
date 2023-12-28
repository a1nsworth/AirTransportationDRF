def update_instance(instance, validated_data):
    for key, value in validated_data.items():
        setattr(instance, key, value)
    return instance
