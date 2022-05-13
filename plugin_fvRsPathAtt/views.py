from django.shortcuts import get_object_or_404, render
from django.views import View
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django_tables2 import LazyPaginator, RequestConfig, SingleTableView
from netbox.views import generic
from django.contrib.auth.mixins import PermissionRequiredMixin
from .icon_classes import icon_classes
from .models import fvRsPathAtt, AciTenant, AciAp, AciEpg
from .tables import fvRsPathAttTable, AciTenantTable, AciApTable, AciEpgTable, fvRsPathAttBulkTable
from .filters import fvRsPathAttFilter , AciTenantFilter, AciApFilter, AciEpgFilter
from .forms import fvRsPathAttForm, fvRsPathAttFilterForm, AciTenantForm , AciTenantFilterForm, AciApFilterForm, AciEpgFilterForm, fvRsPathAttCSVForm
from netbox.views.generic import BulkDeleteView, BulkImportView, ObjectEditView, ObjectListView

'''
One per Class, View, ListView, CreateView, UpdateView, DeleteView
Link to templates, name, name_list, name_edit, name_delete
'''


class fvRsPathAttView(PermissionRequiredMixin, View): # arbitrary class name
    """Display fvRsPathAtt details"""
    permission_required = "plugin_fvRsPathAtt.view_fvRsPathAtt"
    queryset = fvRsPathAtt.objects.all()

    def get(self, request, pk):
        """Get request."""
        fvRsPathAtt_obj = get_object_or_404(self.queryset, pk=pk)

        return render(
            request,
            "plugin_fvRsPathAtt/fvRsPathAtt.html",
            {
                "fvRsPathAtt": fvRsPathAtt_obj,
                "icon_classes": icon_classes,
            },
        )


class fvRsPathAttListView(PermissionRequiredMixin, View):
    """View for listing all existing fvRsPathAtt."""
    permission_required = "plugin_fvRsPathAtt.view_fvRsPathAtt"
    queryset = fvRsPathAtt.objects.all()
    filterset = fvRsPathAttFilter
    filterset_form = fvRsPathAttFilterForm

    def get(self, request):
        """Get request."""
        self.queryset = self.filterset(request.GET, self.queryset).qs.order_by("pk")
        table = fvRsPathAttTable(self.queryset)
        RequestConfig(request, paginate={"per_page": 25}).configure(table)

        return render(
            request, "plugin_fvRsPathAtt/fvRsPathAtt_list.html",
            {
                "table": table,
                "filter_form": self.filterset_form(request.GET),
                "icon_classes": icon_classes,
            },
        )


class fvRsPathAttCreateView(PermissionRequiredMixin, CreateView):
    """View for creating a new fvRsPathAtt instance."""
    permission_required = "plugin_fvRsPathAtt.add_fvRsPathAtt"
    form_class = fvRsPathAttForm
    template_name = "plugin_fvRsPathAtt/fvRsPathAtt_edit.html"

class fvRsPathAttDeleteView(PermissionRequiredMixin, DeleteView):
    """View for deleting a fvRsPathAtt instance."""
    permission_required = "plugin_fvRsPathAtt.delete_fvRsPathAtt"
    model = fvRsPathAtt
    success_url = reverse_lazy("plugins:plugin_fvRsPathAtt:fvRsPathAtt_list")
    template_name = "plugin_fvRsPathAtt/fvRsPathAtt_delete.html"


class fvRsPathAttEditView(PermissionRequiredMixin, UpdateView):
    """View for editing a fvRsPathAtt instance."""
    permission_required = "plugin_fvRsPathAtt.change_fvRsPathAtt"
    queryset = fvRsPathAtt.objects.all()
    model = fvRsPathAtt
    form_class = fvRsPathAttCSVForm
    template_name = "plugin_fvRsPathAtt/fvRsPathAtt_edit.html"

class fvRsPathAttImportView(PermissionRequiredMixin, BulkImportView):
    """View for bulk-importing a CSV file to create .."""

    permission_required = "plugin_fvRsPathAtt.change_fvRsPathAtt"
    queryset = fvRsPathAtt.objects.all()
    model_form = fvRsPathAttCSVForm
    table = fvRsPathAttBulkTable
    default_return_url = "plugins:plugin_fvRsPathAtt:fvRsPathAtt_list"

######################## Tenant stuff ################################################

class AciTenantView(PermissionRequiredMixin, View): # arbitrary class name
    """Display fvRsPathAtt details"""
    permission_required = "plugin_fvRsPathAtt.view_fvRsPathAtt"
    queryset = AciTenant.objects.all() # retrieve and filter interesting objects

    def get(self, request, pk):
        """Get request."""
        AciTenant_obj = get_object_or_404(self.queryset, pk=pk) # asking for single object matching pk. pk means primary key and each of objects will have one.

        return render(
            request,
            "plugin_fvRsPathAtt/AciTenant.html", # Template For Single Object View
            {
                "AciTenant": AciTenant_obj,
                "icon_classes": icon_classes,
            },
        )

class AciTenantListView(PermissionRequiredMixin, View):
    """View for listing all existing fvRsPathAtt."""
    permission_required = "plugin_fvRsPathAtt.view_fvRsPathAtt"
    queryset = AciTenant.objects.all() # retrieve and filter interesting objects
    filterset = AciTenantFilter  # need to create this and import it
    filterset_form = AciTenantFilterForm # need to create this and import it

    def get(self, request):
        """Get request."""
        self.queryset = self.filterset(request.GET, self.queryset).qs.order_by("pk")
        table = AciTenantTable(self.queryset) # need to create this and import it
        RequestConfig(request, paginate={"per_page": 25}).configure(table)

        return render(
            request, "plugin_fvRsPathAtt/AciTenant_list.html",
            {
                "table": table,
                "filter_form": self.filterset_form(request.GET),
                "icon_classes": icon_classes,
            },
        )


######################## Application profile stuff ################################################

class AciApView(PermissionRequiredMixin, View): # arbitrary class name
    """Display fvRsPathAtt details"""
    permission_required = "plugin_fvRsPathAtt.view_fvRsPathAtt"
    queryset = AciAp.objects.all() # retrieve and filter interesting objects

    def get(self, request, pk):
        """Get request."""
        AciAp_obj = get_object_or_404(self.queryset, pk=pk) # asking for single object matching pk. pk means primary key and each of objects will have one.

        return render(
            request,
            "plugin_fvRsPathAtt/AciAp.html", # Template For Single Object View
            {
                "AciAp": AciAp_obj,
                "icon_classes": icon_classes,
            },
        )

class AciApListView(PermissionRequiredMixin, View):
    """View for listing all existing fvRsPathAtt."""
    permission_required = "plugin_fvRsPathAtt.view_fvRsPathAtt"
    queryset = AciAp.objects.all() # retrieve and filter interesting objects
    filterset = AciApFilter  # need to create this and import it
    filterset_form = AciApFilterForm # need to create this and import it

    def get(self, request):
        """Get request."""
        self.queryset = self.filterset(request.GET, self.queryset).qs.order_by("pk")
        table = AciApTable(self.queryset) # need to create this and import it
        RequestConfig(request, paginate={"per_page": 25}).configure(table)

        return render(
            request, "plugin_fvRsPathAtt/AciAp_list.html",
            {
                "table": table,
                "filter_form": self.filterset_form(request.GET),
                "icon_classes": icon_classes,
            },
        )


######################## EPG stuff ################################################

class AciEpgView(PermissionRequiredMixin, View): # arbitrary class name
    """Display fvRsPathAtt details"""
    permission_required = "plugin_fvRsPathAtt.view_fvRsPathAtt"
    queryset = AciTenant.objects.all() # retrieve and filter interesting objects

    def get(self, request, pk):
        """Get request."""
        AciTenant_obj = get_object_or_404(self.queryset, pk=pk) # asking for single object matching pk. pk means primary key and each of objects will have one.

        return render(
            request,
            "plugin_fvRsPathAtt/AciTenant.html", # Template For Single Object View
            {
                "AciTenant": AciTenant_obj,
                "icon_classes": icon_classes,
            },
        )

class AciEpgListView(PermissionRequiredMixin, View):
    """View for listing all existing fvRsPathAtt."""
    permission_required = "plugin_fvRsPathAtt.view_fvRsPathAtt"
    queryset = AciEpg.objects.all() # retrieve and filter interesting objects
    filterset = AciEpgFilter  # need to create this and import it
    filterset_form = AciEpgFilterForm # need to create this and import it

    def get(self, request):
        """Get request."""
        self.queryset = self.filterset(request.GET, self.queryset).qs.order_by("pk")
        table = AciEpgTable(self.queryset) # need to create this and import it
        RequestConfig(request, paginate={"per_page": 25}).configure(table)

        return render(
            request, "plugin_fvRsPathAtt/AciEpg_list.html",
            {
                "table": table,
                "filter_form": self.filterset_form(request.GET),
                "icon_classes": icon_classes,
            },
        )