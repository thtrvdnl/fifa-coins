from django.contrib.auth import get_user_model
from rest_framework import serializers, validators

CustomUser = get_user_model()


class CustomUserCreateSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(
        write_only=True,
        validators=[
            validators.UniqueValidator(
                message="This full name already exists",
                queryset=CustomUser.objects.all(),
            )
        ],
    )
    email = serializers.CharField(
        write_only=True,
        validators=[
            validators.UniqueValidator(
                message="This email already exists", queryset=CustomUser.objects.all()
            )
        ],
    )
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ("full_name", "email", "password")


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("full_name", "email")
