from django.contrib import admin
from  .models import Team


class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
    # list_filter = ['prize_pool', 'is_active',]
    search_fields = ['name',]
    # when editing an existing model instance.
    fieldsets = (
        (None, {"fields": ("name","members","description","created_at","team_logo","team_banner")}),
        ("Permissions", {"fields": ()}),
    )
    # when adding a new model instance.
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "name","description","team_logo",
            )}
        ),
    )


admin.site.register(Team, TeamAdmin)