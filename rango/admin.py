from django.contrib import admin
from rango.models import Category, Page

<<<<<<< HEAD
class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "url")

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

=======

class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "url")

>>>>>>> d190ee4b4c84f751e4a72bef2f87a85974532ca7
admin.site.register(Category)
admin.site.register(Page, PageAdmin)