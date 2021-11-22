from rest_framework import serializers

from .models import MyUser


class Registerserializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, write_only=True, required=True)
    password_confirmation = serializers.CharField(min_length=8, write_only=True, required=True)

    class Meta:
        model = MyUser
        fields = ('phone_number', 'username', 'password', 'password_confirmation')

    def validate_phone_number(self, phone_number):
        if not phone_number.startswith('+996'):
            raise serializers.ValidationError('You should have a kyrgyz number')
        return phone_number

    def validate(self, attrs):
        password = attrs.get('password')
        password_conf = attrs.pop('password_confirmation')
        if password != password_conf:
            raise serializers.ValidationError('Passwords do not match')
        return attrs

    def create(self, validated_data):
        user = MyUser.objects.create_user(**validated_data)
        send_activation_sms()