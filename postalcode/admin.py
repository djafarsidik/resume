from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Provinsi, Kab_kota

# Register your models here.

class ProvinsiResource(resources.ModelResource):
    fields = ['code','nama']
    
    class Meta:
        model = Provinsi

class KabkotaResource(resources.ModelResource):
    fields = ['code','nama', 'type', 'provinsi']
    
    class Meta:
        model = Kab_kota

class ProvinsiAdmin(ImportExportModelAdmin):
    resource = ProvinsiResource
    search_fields = ['nama']
    list_display = ['code','nama']
    
class KabkotaAdmin(ImportExportModelAdmin):
    resource = KabkotaResource
    autocomplete_fields = ['provinsi']
    search_fields = ['nama']
    list_filter = ['provinsi']
    list_display = ['code','nama', 'type', 'provinsi']
    
admin.site.register(Provinsi, ProvinsiAdmin)
admin.site.register(Kab_kota, KabkotaAdmin)