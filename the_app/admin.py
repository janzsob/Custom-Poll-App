from django.contrib import admin
from .models import Students, Blog, Listings

admin.site.register(Students)


class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('post_date', 'update_date')


admin.site.register(Blog, BlogAdmin)

admin.site.register(Listings)
