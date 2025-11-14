from django.contrib import admin
from notes.models import Note

class NoteAdmin(admin.ModelAdmin):
    fields = ['title', 'content', 'category', 'author']
    list_display = ['title', 'author', 'category']
    list_filter = ['created_at', 'author']

admin.site.register(Note, NoteAdmin)