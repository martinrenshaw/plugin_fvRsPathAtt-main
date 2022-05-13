from django.http import HttpResponse
from django.urls import path
from .views import (fvRsPathAttView, 
                    fvRsPathAttListView, 
                    fvRsPathAttCreateView, 
                    fvRsPathAttDeleteView , 
                    fvRsPathAttEditView, 
                    AciTenantView, 
                    AciTenantListView,
                    AciApListView,
                    AciApView,
                    AciEpgListView,
                    AciEpgView,
                    fvRsPathAttImportView,)


urlpatterns = [
    path("", fvRsPathAttListView.as_view(), name="fvRsPathAtt_list"),
    path("<int:pk>/", fvRsPathAttView.as_view(), name="fvRsPathAtt"),
    path("add/", fvRsPathAttCreateView.as_view(), name="fvRsPathAtt_add"),
    path("import/", fvRsPathAttImportView.as_view(), name="fvRsPathAtt_import"),
    path("<int:pk>/delete/", fvRsPathAttDeleteView.as_view(), name="fvRsPathAtt_delete"),
    path("<int:pk>/edit/", fvRsPathAttEditView.as_view(), name="fvRsPathAtt_edit"),
    ######### AciTenant #################################
    path("aci-tenant/", AciTenantListView.as_view(), name="AciTenant_list"),
    path("aci-tenant/<int:pk>/", AciTenantView.as_view(), name="AciTenant"),
    ######### Aci Application profile #################################
    path("aci-ap/", AciApListView.as_view(), name="AciAp_list"),
    path("aci-ap/<int:pk>/", AciApView.as_view(), name="AciAp"),
    ######### Aci End Point groups #################################
    path("aci-epg/", AciEpgListView.as_view(), name="AciEpg_list"),
    path("aci-epg/<int:pk>/", AciEpgView.as_view(), name="AciEpg"),
]