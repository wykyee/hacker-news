from rest_framework import serializers

from django.contrib.auth import get_user_model


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "password",
            "password2",
            "first_name",
            "last_name",
            "email",
            "id",
        )
        read_only_fields = ("id",)

    def create(self, validated_data):
        """
        User create method, checks if such username
        doesn't exist and passwords are similar.
        """
        password = validated_data.pop("password")
        password2 = validated_data.pop("password2")

        user_model = get_user_model()

        if password != password2:
            raise serializers.ValidationError(
                {"Password": "Provided two different passwords"}
            )
        new_user = user_model(**validated_data)
        new_user.set_password(password)
        new_user.save()
        return new_user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "date_joined",
            "last_login",
            "id",
        )
        read_only_fields = ("username", "id", "date_joined", "last_login")
