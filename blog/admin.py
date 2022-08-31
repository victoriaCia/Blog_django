from django.contrib import admin
from .models import Blog, Author, Entry


class BlogAdmin(admin.ModelAdmin):
    pass

class AuthorAdmin(admin.ModelAdmin):
    pass

class EntryAdmin(admin.ModelAdmin):
    list_display = ('headline', 'blog', 'pub_date')
    date_hierarchy = 'pub_date'
    readonly_fields = ('pub_date',)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Entry, EntryAdmin)