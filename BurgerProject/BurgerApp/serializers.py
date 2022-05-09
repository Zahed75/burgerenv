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


# ==============Order Serializers========= Nesting Serializer


class IngredientSerializer(ModelSerializer):
    class Meta:
        model = Ingredient
        exclude = ["id"]


class CustomerDetailSerializer(ModelSerializer):
    class Meta:
        model = CustomerDetail
        fields = '__all__'


class OrderSerializer(ModelSerializer):
    ingredients = IngredientSerializer()
    customer = CustomerDetailSerializer()

    class Meta:
        model = Order
        fields = "__all__"

    def create(self, validated_data):
        ingredient_data = validated_data.pop("ingredients")
        customer_data = validated_data.pop("customer")
        ingredients = IngredientSerializer.create(
            IngredientSerializer(), validated_data=ingredient_data
        )
        customer = CustomerDetailSerializer.create(
            CustomerDetailSerializer(), validated_data=customer_data
        )
        order, created = Order.objects.update_or_create(
            ingredients=ingredients,
            customer=customer,
            price=validated_data.pop("price"),
            orderTime=validated_data.pop("orderTime"),
            user=validated_data.pop("user"),
        )

        return order
