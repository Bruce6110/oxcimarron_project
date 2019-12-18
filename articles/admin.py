from django.contrib import admin

from .models import Article, Comment


class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 0


class CommentAdmin(admin.ModelAdmin):
    #display the specified properties for each comment
    list_display = ('author', 'comment', 'article', 'created_date', 'approved')
    
    #filter comments based on fields specified
    list_filter=('approved','created_date')

    #search on specified fields
    search_fields=('author','comment')

    #allows for approving many comments at once
    actions= ['approve_comments']

    def approve_comments(self,request,queryset):
        queryset.update(active=True)

class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInLine, ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
