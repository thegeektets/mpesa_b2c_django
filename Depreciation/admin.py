from django.contrib import admin

from .models import User
from .models import Assets
from .models import Depreciation

admin.site.register(User)
admin.site.register(Assets)
admin.site.register(Depreciation)