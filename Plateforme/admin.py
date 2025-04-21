from django.contrib import admin

# Register your models here.
class AdminArea(admin.AdminSite):
    index_title = "Administration"
    site_header = "GP ADMIN"
    site_title = "Site PFE"