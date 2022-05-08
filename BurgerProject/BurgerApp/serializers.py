from rest_framework.serializers import ModelSerializer
# from django.contrib.auth.hashers import make_password
from .models import *
from rest_framework import serializers


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
            "id",
            "email",
            "password",
        )
        extra_kwargs = {
            "password": {"write_only": True, "style": {"input_type": "password"}}
        }

    def create(self, validated_data):
        user = UserProfile.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
        )

        return user


# 2nd method to create HASH Pass to create a user you can use anyone this make sure import
# from django.contrib.auth.hashers import make_password


# def create(self, validated_data):
#     password = validated_data.pop('password', None)
#     instance = self.Meta.model(**validated_data)
#
#     # Adding the below line made it work for me.
#     instance.is_active = True
#     if password is not None:
#         # Set password does the hash, so you don't need to call make_password
#         instance.set_password(password)
#     instance.save()
#     return instance


# ==============Order Serializers=========


class IngredientSerializer(ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


class OrderSerializer(ModelSerializer):
    ingredients = IngredientSerializer()

    class Meta:
        model = Order
        fields = "__all__"
