from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.conf import settings

from .tasks import send_activation_sms, send_activation_code
from .utils import normalize_phone


User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):

    password_confirm = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'phone', 'password', 'password_confirm', 'code_confirm_method')

    def validate_phone(self, phone):
        if len(phone) != 13:
            raise serializers.ValidationError('Неправильный формат номера телефона.')
        return phone

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.pop('password_confirm')
        if password != password_confirm:
            raise serializers.ValidationError('Пароли не совпадают.')
        return attrs

    def create(self, validated_data): 
        user = User.objects.create_user(**validated_data)
        user.create_activation_code()
        if validated_data['code_confirm_method'] == 'email':
            send_activation_code(user.email, user.activation_code)
        if validated_data['code_confirm_method'] == 'phone':
            send_activation_sms(user.phone, user.activation_code) # delay
        return user 


class ActivationSerializer(serializers.Serializer):
    username = serializers.ReadOnlyField(source='user.username') # потому что телефон не unique
    phone = serializers.CharField(max_length=13, required=True)
    code = serializers.CharField(max_length=10, required=True)

    def validate_phone(self, phone):
        phone = normalize_phone(phone)
        if len(phone) != 13:
            raise serializers.ValidationError('Неправильный формат номера телефона.')
        if not User.objects.filter(phone=phone).exists():
            raise serializers.ValidationError('Пользователя с таким номером телефона не существует.')
        return phone

    def validate_code(self, code):
        if not User.objects.filter(activation_code=code).exists():
            raise serializers.ValidationError('Invalid activation code')

    def activate_account(self):
        phone = self.validated_data.get('phone')
        user = User.objects.get(phone=phone)
        user.is_active = True
        user.activation_code = ''
        user.save()


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=150, required=True)
    new_password = serializers.CharField(max_length=150, required=True)
    new_password_confirm = serializers.CharField(max_length=150, required=True)

    def validate_old_password(self, old_password):
        user = self.context.get('request').user
        if not user.check_password(old_password):
            raise serializers.ValidationError('Неправильнвй пароль!'.upper())
        return old_password

    def validate(self, attrs: dict):
        new_password = attrs.get('new_password')
        new_password_confirm = attrs.get('new_password_confirm')
        if new_password != new_password_confirm:
            raise serializers.ValidationError(
                'Пароли не совпадают.'
            )
        return attrs

    def set_new_password(self):
        user = self.context.get('request').user
        password = self.validated_data.get('new_password')
        user.set_password(password)
        user.save()


class RestorePasswordSerializer(serializers.Serializer):

    phone = serializers.CharField(max_length=13, required=True)

    def validate_phone(self, phone):
        phone = normalize_phone(phone)
        if len(phone) != 13:
            raise serializers.ValidationError('Неправильный формат номера телефона.')
        return phone

    def send_code(self):
        phone = self.validated_data.get('phone')
        user = User.objects.get(phone=phone) 
        user.create_activation_code()
        send_activation_sms(user.phone, user.activation_code)


class SetRestoredPasswordSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=13, required=True)
    code = serializers.CharField(min_length=1, max_length=10, required=True)
    new_password = serializers.CharField(max_length=128, required=True)
    new_password_confirm = serializers.CharField(max_length=128, required=True)

    def validate_code(self, code):
        if not User.objects.filter(activation_code=code).exists():
            raise serializers.ValidationError(
                'Некорректный код.'
            )
        return code 

    def validate(self, attrs):
        new_password = attrs.get('new_password')
        new_password_confirm = attrs.get('new_password_confirm')
        if new_password != new_password_confirm:
            raise serializers.ValidationError(
                'Пароли не совпадают.'
            )
        return attrs

    def validate_phone(self, phone):
        phone = normalize_phone(phone)
        if len(phone) != 13:
            raise serializers.ValidationError('Неправильный формат номера телефона.')
        return phone

    def set_new_password(self): 
        phone = self.validated_data.get('phone')
        user = User.objects.get(phone=phone)
        new_password = self.validated_data.get('new_password')
        user.set_password(new_password)
        user.activation_code = ''
        user.save()