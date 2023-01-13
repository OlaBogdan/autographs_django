from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Person, Address, Letter
from .serializers import MiniPersonSerializer, BasicPersonSerializer, ExtendedPersonSerializer
from .serializers import MiniAddressSerializer, BasicAddressSerializer
from .serializers import MiniLetterSerializer, BasicLetterSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = BasicPersonSerializer

    @action(detail=True)
    def letters(self, request, **kwargs):
        person = self.get_object()
        letters = person.letters

        serializer = BasicLetterSerializer(letters, many=True)

        return Response(serializer.data)

    @action(detail=True)
    def letters_with_response(self, request, **kwargs):
        person = self.get_object()
        letters = person.letters.filter(is_responded=True)

        serializer = BasicLetterSerializer(letters, many=True)

        return Response(serializer.data)

    @action(detail=True)
    def letters_without_response(self, request, **kwargs):
        person = self.get_object()
        letters = person.letters.filter(is_responded=False)

        serializer = BasicLetterSerializer(letters, many=True)

        return Response(serializer.data)

    @action(detail=True)
    def addresses(self, request, **kwargs):
        person = self.get_object()
        addresses = person.addresses

        serializer = BasicAddressSerializer(addresses, many=True)

        return Response(serializer.data)


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = BasicAddressSerializer


class LetterViewSet(viewsets.ModelViewSet):
    queryset = Letter.objects.all()
    serializer_class = BasicLetterSerializer
