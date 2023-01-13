from rest_framework import serializers

from .models import Person, Address, Letter


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True)

    class Meta:
        model = Person
        fields = '__all__'


class MiniPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name']


class LetterSerializer(serializers.ModelSerializer):
    # address = AddressSerializer(many=False)
    # to_whom = MiniPersonSerializer(many=False)

    class Meta:
        model = Letter
        fields = '__all__'
