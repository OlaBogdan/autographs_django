from rest_framework import serializers

from .models import Person, Address, Letter


class MiniPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name']


class MiniAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        exclude = ['person', ]


class MiniLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Letter
        exclude = ['to_whom', 'address']


class BasicPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class BasicAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class BasicLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Letter
        fields = '__all__'


class ExtendedPersonSerializer(serializers.ModelSerializer):
    addresses = MiniAddressSerializer(many=True)
    letters = MiniLetterSerializer(many=True)

    class Meta:
        model = Person
        fields = '__all__'
