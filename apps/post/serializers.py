from rest_framework import serializers

from .models import Storage
from .utils import normalize_phone

class StorageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = ('storage','user', 'title', 'image', 'status', 'text', 'category', 'address', 'date' )


# class StorageSerializer(serializers.ModelSerializer):
#     user = serializers.ReadOnlyField(source='user.username')

#     class Meta:
#         model = Storage
#         fields = ('storage','user', 'title', 'image', 'status', 'text', 'category', 'address', 'date' )


class StorageImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = 'image',


class StorageCreateSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(
        default=serializers.CurrentUserDefault(),
        source='user.username'
    )

    class Meta:
        model = Storage
        fields = '__all__'
        
    def validate_whatsapp(self, whatsapp):
        whatsapp = normalize_phone(whatsapp)
        if len(whatsapp) != 13:
            raise serializers.ValidationError('Не верный формат телефона')
        return whatsapp 
        
    def create(self, validated_data):
        post = Storage.objects.create(**validated_data)
        return post

