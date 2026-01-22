#transforms our model into json data so we can access in our api
from rest_framework import serializers
from .models import User


class UserSerilaizer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields = '__all__'