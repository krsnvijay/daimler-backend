from django.contrib import admin

# Register your models here.
from sos.models import Comment, Sos


class CommentInline(admin.TabularInline):
    model = Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ['posted_by', 'sosid', 'partid']
    list_display = 'id', 'posted_by', 'content', 'date'


@admin.register(Sos)
class SosAdmin(admin.ModelAdmin):
    inlines = (CommentInline,)
    search_fields = ['id', 'posted_by']
    list_filter = ('level',)
    list_display = 'id', 'name', 'posted_by', 'content', 'level', 'status', 'date',
