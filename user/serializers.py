from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    

    class Meta:
        model = User
        fields = ['name', 'last_name', 'username', 'email']

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.save()
        return user
