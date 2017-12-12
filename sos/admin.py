from django.contrib import admin

# Register your models here.
from sos.models import Comment


class CommentInline(admin.TabularInline):
    model = Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ['posted_by', 'partid']
    list_display = 'id', 'posted_by', 'content', 'date'

