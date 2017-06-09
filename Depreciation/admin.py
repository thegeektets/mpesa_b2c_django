from django.contrib import admin


from .models import Assets
from .models import Depreciation

admin.site.register(Assets)
admin.site.register(Depreciation)