from django.contrib import admin
from .models import Book

# Register your models here.

from django.contrib import admin
from .models import Book

# Customizing the admin interface for the Book model
class BookAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ("title", "author", "publication_year")
    
    # Enable filtering by these fields in the sidebar
    list_filter = ("author", "publication_year")
    
    # Enable searching by title
    search_fields = ("title",)

# Register the model with the custom class
admin.site.register(Book, BookAdmin)