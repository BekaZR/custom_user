from dataclasses import fields
from rest_framework import serializers

from mainapp.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'email', 'user_name', 'first_name', 
            'start_date', 'about', 'password',
        )
        read_only_fields = (
            'start_date',
        )
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user