from django.contrib import admin
from .models import fvRsPathAtt, AciTenant, AciAp, AciEpg

@admin.register(fvRsPathAtt)
class fvRsPathAttAdmin(admin.ModelAdmin):
    list_display = ("site", "encap_id", "pod_id", "leafs_id", "ap", "epg", "interface", "change_ref")

@admin.register(AciTenant)
class AciTenantAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(AciAp)
class AciTenantAdmin(admin.ModelAdmin):
    list_display = ('name', 'aci_tenant' ,'description')

@admin.register(AciEpg)
class AciTenantAdmin(admin.ModelAdmin):
    list_display = ('name', 'aci_ap' , 'description')