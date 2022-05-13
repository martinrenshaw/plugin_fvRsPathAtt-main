import django_filters
from django.db.models import Q

from dcim.models import Device, Site

from .models import fvRsPathAtt, AciTenant, AciAp, AciEpg


class fvRsPathAttFilter(django_filters.FilterSet):
    """Filter capabilities for fvRsPathAtt instances."""

    q = django_filters.CharFilter(
        method="search",
        label="Search",
    )

    site = django_filters.ModelMultipleChoiceFilter(
        field_name="site__slug",
        queryset=Site.objects.all(),
        to_field_name="slug",
    )

    class Meta:
        model = fvRsPathAtt

        fields = [
            "pod_id",
            "leafs_id",
            "ap",
            "epg",
            "interface",
            "change_ref"
        ]

    def search(self, queryset, name, value):
        """Perform the filtered search."""
        if not value.strip():
            return queryset
        qs_filter = (Q(change_ref__icontains=value) | Q(epg__icontains=value))
        return queryset.filter(qs_filter)

class AciTenantFilter(django_filters.FilterSet):
    """Filter capabilities for fvRsPathAtt instances."""

    q = django_filters.CharFilter(
        method="search",
        label="Search",
    )

    site = django_filters.ModelMultipleChoiceFilter(
        field_name="site__slug",
        queryset=Site.objects.all(),
        to_field_name="slug",
    )

    class Meta:
        model = AciTenant

        fields = [
            "name",
            "description",
 
        ]

    def search(self, queryset, name, value):
        """Perform the filtered search."""
        if not value.strip():
            return queryset
        qs_filter = (Q(change_ref__icontains=value) | Q(epg__icontains=value))
        return queryset.filter(qs_filter)


class AciApFilter(django_filters.FilterSet):
    """Filter capabilities for fvRsPathAtt instances."""

    q = django_filters.CharFilter(
        method="search",
        label="Search",
    )

    site = django_filters.ModelMultipleChoiceFilter(
        field_name="site__slug",
        queryset=Site.objects.all(),
        to_field_name="slug",
    )

    class Meta:
        model = AciTenant

        fields = [
            "name",
            "description",
 
        ]

    def search(self, queryset, name, value):
        """Perform the filtered search."""
        if not value.strip():
            return queryset
        qs_filter = (Q(change_ref__icontains=value) | Q(epg__icontains=value))
        return queryset.filter(qs_filter)

class AciEpgFilter(django_filters.FilterSet):
    """Filter capabilities for fvRsPathAtt instances."""

    q = django_filters.CharFilter(
        method="search",
        label="Search",
    )

    site = django_filters.ModelMultipleChoiceFilter(
        field_name="site__slug",
        queryset=Site.objects.all(),
        to_field_name="slug",
    )

    class Meta:
        model = AciEpg

        fields = [
            "name",
            "description",
 
        ]

    def search(self, queryset, name, value):
        """Perform the filtered search."""
        if not value.strip():
            return queryset
        qs_filter = (Q(change_ref__icontains=value) | Q(epg__icontains=value))
        return queryset.filter(qs_filter)