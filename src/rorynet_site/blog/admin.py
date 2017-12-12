from django.contrib import admin
from .models import Blog, Category

# admin.site.register(Blog)
# admin.site.register(Category)

class BlogAdmin(admin.ModelAdmin):
    print("Blog Admin")
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)} # Slug is the url

class CategoryAdmin(admin.ModelAdmin):
    print("Category Admin")
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
