from django.contrib import admin
from .models import Category, Post, UserProfile, Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class CommentInline(admin.TabularInline):
    model = Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted', 'category','status')
    list_filter = ('category', 'author', 'date_posted')
    search_fields = ('title', 'content', 'author__username', 'category__name')
    inlines = [CommentInline]

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'university', 'country', 'city', 'avatar')
    search_fields = ('user__username', 'user__email', 'university', 'country', 'city')

admin.site.register(UserProfile, UserProfileAdmin)
