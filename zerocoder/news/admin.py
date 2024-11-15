from django.contrib import admin
from .models import NewsPost

# admin.site.register(NewsPost)

@admin.register(NewsPost)
class NewsPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date')