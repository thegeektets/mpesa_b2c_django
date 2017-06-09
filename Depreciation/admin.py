from django.contrib import admin


from .models import Assets
from .models import Depreciation
from .models import User

admin.site.register(User)
admin.site.register(Assets)
admin.site.register(Depreciation)