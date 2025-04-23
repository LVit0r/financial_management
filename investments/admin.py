from django.contrib import admin
from investments.models import Entry

class EntryAdmin(admin.ModelAdmin):
    list_display = ('value', 'origin', 'date',)
    search_fields = ('origin',)

admin.site.register(Entry, EntryAdmin)
