from django.contrib import admin
from .models import businessForm, Fleet, ReplyCus, Airports, City, Rates, SchoolContract, TrackSchoolContract, Schedule

# Register your models here.

admin.site.register(businessForm)
admin.site.register(Fleet)
admin.site.register(ReplyCus)
admin.site.register(Airports)
admin.site.register(City)
admin.site.register(Rates)
admin.site.register(SchoolContract)
admin.site.register(TrackSchoolContract)
admin.site.register(Schedule)