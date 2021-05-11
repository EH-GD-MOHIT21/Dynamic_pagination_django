from django.contrib import admin

# Register your models here.

from .models import paginationdata as pad
from .models import generalpagination as gpag

admin.site.register(pad)
admin.site.register(gpag)

admin.site.site_header = "Pagination Admin"
admin.site.site_title = "Welcome to Pagination admin"
admin.site.index_title = "Hello World to Pagination"