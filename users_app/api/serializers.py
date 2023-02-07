from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from users_app.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'bio', 'image')
        extra_kwargs = {
            'first_name': {'required': True}
        }

    def update(self, instance, validated_data):
        exist_usernames = CustomUser.objects.filter(username__iexact=validated_data['username']).exclude(pk=instance.pk)
        if exist_usernames.exists():
            raise ValidationError({
                'username': "A user with that username already exists.",
            })

        return super().update(instance, validated_data)


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, style={"input_type": "password"})

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password', 'password2', 'bio', 'image')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {"input_type": "password"},
            },
        }

    def validate_username(self, value):
        if CustomUser.objects.filter(username__iexact=value).exists():
            raise ValidationError("A user with that username already exists.")
        return value

    def validate(self, data):
        # To check passwords matching
        if data['password'] != data['password2']:
            raise ValidationError({'error': 'Passwords should be the same!'})

        return data

    def save(self, **kwargs):
        super().save()
        data = self.validated_data
        data.pop("password2")
        password = data.pop("password")

        account = CustomUser(**data)
        account.set_password(password)
        account.save()
        self.instance = account

        return self.instance

    def to_representation(self, instance):
        # print(instance)
        data = super().to_representation(instance)
        # print(data)
        data.update(instance.get_tokens())
        return data
