from django.contrib import admin
from .models import Board, Property, Player


class PropertyInline(admin.StackedInline):
    model = Property
    max_num = 20
    extra = 1


class BoardAdmin(admin.ModelAdmin):
    model = Board
    inlines = (PropertyInline,)
    list_display = ('name',)


admin.site.register(Board, BoardAdmin)
admin.site.register(Player)
