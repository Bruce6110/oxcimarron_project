from django.contrib import admin

from .models import Author
from .models import Book
from django.contrib import admin

# Register your models here.

admin.ModelAdmin.list_per_page = 1000

from .models import Book, Author


class BookInLine(admin.TabularInline):
    model = Book
    extra = 0


class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInLine, ]
   


admin.site.register(Author, AuthorAdmin)


admin.site.register(Book)
