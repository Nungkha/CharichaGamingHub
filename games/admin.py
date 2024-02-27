from django.contrib import admin
from . models import Game


class GameAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'genre', 'rating', 'published_by', 'developed_by']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['genre', 'rating',]
    search_fields = ['name','genre',]
    fieldsets = (
        (None, {"fields": ("name", "slug","genre","rating", "thumbnail","game_cover","published_by","developed_by", "description", "price", "platform","release_date")}),
        ("Permissions", {"fields": ()}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "name", "slug", "genre","thumbnail","game_cover","published_by","developed_by", "description","release_date"
            )}
        ),
    )


admin.site.register(Game, GameAdmin)
