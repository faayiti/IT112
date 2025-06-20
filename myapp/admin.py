from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre')
    search_fields = ('title', 'author')
    list_filter = ('genre',)

admin.site.register(Book, BookAdmin)
