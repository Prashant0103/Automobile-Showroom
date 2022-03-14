from email.errors import CloseBoundaryNotFoundDefect
from django.contrib import admin
from auto.models import car,Customer,contact

admin.site.register(car)
admin.site.register(Customer)
admin.site.register(contact)