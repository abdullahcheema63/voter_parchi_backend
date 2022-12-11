from django.contrib import admin

from api.models import VoterRecord


# Register your models here.

class VoterRecordAdmin(admin.ModelAdmin):
    list_display = ['identity_number', 'block_code', 'polling_station', 'polling_booth']
    list_filter = ['block_code', 'polling_station', 'polling_booth']
    search_fields = ['identity_number']


admin.site.register(VoterRecord, VoterRecordAdmin)
