from django.contrib import admin
from .models import Word


class WordAdmin(admin.ModelAdmin):
    list_display = ('rus_word', 'eng_word')
    search_fields = ('rus_word', 'eng_word')
    list_filter = ('meta_add_date',)
    empty_value_display = "-пусто-"


admin.site.register(Word, WordAdmin)
