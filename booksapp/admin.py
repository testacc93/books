from booksapp.models import Book
from django.contrib import admin
from booksapp.models import Book, User

class BookAdmin(admin.ModelAdmin):
    list_display = ['name','min_age', 'image']

admin.site.register(Book, BookAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ['username','age', 'created']

admin.site.register(User, UserAdmin)