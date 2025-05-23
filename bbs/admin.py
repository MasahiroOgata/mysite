from django.contrib import admin
from .models import Article

@admin.register(Article)
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ['id',]
