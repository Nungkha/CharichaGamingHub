from django.contrib import admin
from . models import Game


class GameAdmin(admin.ModelAdmin):
    list_display = ['name', 'genre', 'rating', 'published_by', 'developed_by']
    list_filter = ['genre', 'rating',]
    search_fields = ['name','genre',]
    fieldsets = (
        (None, {"fields": ("name", "genre","rating", "thumbnail","published_by","developed_by", "description", "price", "platform","release_date")}),
        ("Permissions", {"fields": ()}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "name", "genre","thumbnail","published_by","developed_by", "description",
            )}
        ),
    )


admin.site.register(Game, GameAdmin)
