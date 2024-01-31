from django.contrib import admin
from blog.models import Post, Comment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    fields =['created_date', 'title','text']
    search_fields =['title']
    list_filter = ['created_date']
    list_display =['author','created_date','text']
    list_editable= ['text']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)