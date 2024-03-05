from django.contrib import admin
from  .models import Space


class SpaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
    # list_filter = ['prize_pool', 'is_active',]
    search_fields = ['name',]
    # when editing an existing model instance.
    fieldsets = (
        (None, {"fields": ("name", "admin","members","description","created_at","space_logo","space_banner")}),
        ("Permissions", {"fields": ()}),
    )
    # when adding a new model instance.
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "name", "admin","description","slug", "space_logo",
            )}
        ),
    )


admin.site.register(Space, SpaceAdmin)
