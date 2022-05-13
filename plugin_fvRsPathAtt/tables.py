import django_tables2 as tables
from utilities.tables import BaseTable, ToggleColumn
from .models import fvRsPathAtt, AciTenant, AciAp, AciEpg


class fvRsPathAttTable(BaseTable):
    """Table for displaying fvRsPathAtt objects."""

    pk = ToggleColumn()
    id = tables.LinkColumn()
    site = tables.LinkColumn()
    # device = tables.LinkColumn()
    # local_ip = tables.LinkColumn()

    class Meta(BaseTable.Meta):
        model = fvRsPathAtt
        fields = (
            "pk",
            "id",
            "site",
            "encap_id",
            "pod_id",
            "leafs_id",
            "ap",
            "epg",
            "interface",
            "change_ref",
        )

class fvRsPathAttBulkTable(BaseTable):
    """Table for bulk import offvRsPathAtt objects."""

    pk = ToggleColumn()
    id = tables.LinkColumn()
    # site = tables.LinkColumn()
    # device = tables.LinkColumn()
    # local_ip = tables.LinkColumn()

    class Meta(BaseTable.Meta):
        model = fvRsPathAtt
        fields = (
            "pk",
            "id",
            "site",
            "encap_id",
            "pod_id",
            "leafs_id",
            "ap",
            "epg",
            "interface",
            "change_ref",
        )

class AciTenantTable(BaseTable):
    """Table for displaying fvRsPathAtt objects."""

    pk = ToggleColumn()
    id = tables.LinkColumn()
    name = tables.LinkColumn()
    # device = tables.LinkColumn()
    # local_ip = tables.LinkColumn()

    class Meta(BaseTable.Meta):
        model = AciTenant
        fields = (
            "pk",
            "id",
            "name",
            "description",

        )

class AciApTable(BaseTable):
    """Table for displaying fvRsPathAtt objects."""

    pk = ToggleColumn()
    id = tables.LinkColumn()
    aci_tenant = tables.LinkColumn()
    name = tables.LinkColumn()
    # device = tables.LinkColumn()
    # local_ip = tables.LinkColumn()

    class Meta(BaseTable.Meta):
        model = AciAp
        fields = (
            "pk",
            "id",
            "name",
            "aci_tenant",
            "description",

        )

class AciEpgTable(BaseTable):
    """Table for displaying fvRsPathAtt objects."""

    pk = ToggleColumn()
    id = tables.LinkColumn()
    aci_ap = tables.LinkColumn()
    name = tables.LinkColumn()
    # local_ip = tables.LinkColumn()

    class Meta(BaseTable.Meta):
        model = AciEpg
        fields = (
            "pk",
            "id",
            "name",
            # "site",
            "aci_ap",
            "description",

        )