from django.contrib import admin
from.models import MainContent, Comment

class MainContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'pub_date']
    search_fields = ['title']

class ContentAdmin(admin.ModelAdmin):
    list_display = ['content_list', 'content', 'author', 'create_date', 'modify_date']
    search_fields = ['author']

admin.site.register(MainContent, MainContentAdmin)
admin.site.register(Comment, ContentAdmin)
# Register your models here.
