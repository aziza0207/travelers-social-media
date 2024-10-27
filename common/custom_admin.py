from django.contrib import admin


class ReadOnlyAdmin(admin.ModelAdmin):
    """ Базовый класс админки, который делает модели только для чтения в интерфейсе администрирования. """

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
