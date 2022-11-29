from django.contrib import admin


from .models import BusinessProfile, Guide, Tour


admin.site.register(BusinessProfile)
admin.site.register(Guide)
admin.site.register(Tour)