from django.contrib import admin
from api.models import *


admin.site.register(Todo)
admin.site.register(Folder)
admin.site.register(Status)
admin.site.register(Variation)
admin.site.register(Variation_value_input)

