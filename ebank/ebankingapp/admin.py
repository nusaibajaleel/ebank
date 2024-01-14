from django.contrib import admin
from.models import District,Branch,Account
# Register your models here.
class DistrictAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {"slug": ["name", ]}

admin.site.register(District,DistrictAdmin)
class BranchAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {"slug": ["name", ]}

    list_per_page=5
admin.site.register(Branch,BranchAdmin)
class AccountAdmin(admin.ModelAdmin):
    list_display=['name']
admin.site.register(Account,AccountAdmin)