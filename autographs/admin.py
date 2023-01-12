from django.contrib import admin
from .models import Person, Address, Letter

admin.site.register(Person)
admin.site.register(Address)
admin.site.register(Letter)
