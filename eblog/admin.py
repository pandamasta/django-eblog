from django.contrib import admin

from models import Category
from models import Entry

from django_summernote.admin import SummernoteModelAdmin

class CategoryAdmin(admin.ModelAdmin):
    """
    Administration interface options of ``Category`` model.
    """
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug', 'creation_date', 'modification_date')
    search_fields = ('name',)
    #date_hierarchy = 'creation_date'
    save_on_top = True
    prepopulated_fields = {'slug': ('name',)}


#class EntryAdmin(admin.ModelAdmin):
class EntryAdmin(SummernoteModelAdmin):
    """
    Administration interface options of ``Entry`` model.
    """
    list_display = ('title', 'category', 'status', 'author')
    search_fields = ('title', 'body')
    #date_hierarchy = 'publication_date'
    save_on_top = True
    radio_fields = {'status': admin.VERTICAL}
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Entry, EntryAdmin)

