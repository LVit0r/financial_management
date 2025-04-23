from django.contrib import admin
from expenses.models import Status, Expenses


class StatusAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Status, StatusAdmin)


class ExpensesAdmin(admin.ModelAdmin):
    list_display = ('exp_name', 'status', 'value', 'payday', )
    search_fields = ('exp_name',)

admin.site.register(Expenses, ExpensesAdmin)
