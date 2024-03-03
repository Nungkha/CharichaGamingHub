from django.contrib import admin
from . models import Tournament


class TournamentAdmin(admin.ModelAdmin):
    list_display = ['name', 'game', 'organizer', 'prize_pool', 'is_active']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['prize_pool', 'is_active',]
    search_fields = ['name','game',]
    # when editing an existing model instance.
    fieldsets = (
        (None, {"fields": ("name", "game","slug","prize_pool","organizer", "description","partner", 
                    "registration_deadline","start_time","end_time", "location","entry_fee","max_players",
                        "rules","is_active","thumbnail")}),
        ("Permissions", {"fields": ()}),
    )
    # when adding a new model instance.
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "name", "game","organizer","slug", "thumbnail",
            )}
        ),
    )


admin.site.register(Tournament, TournamentAdmin)

