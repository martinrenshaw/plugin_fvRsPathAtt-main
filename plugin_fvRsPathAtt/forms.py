from django import forms
from dcim.models import Device, Site
from ipam.models import VLAN
from utilities.forms import BootstrapMixin
from extras.forms import CustomFieldModelCSVForm
from .models import fvRsPathAtt, AciTenant, AciAp, AciEpg


class fvRsPathAttForm(BootstrapMixin, forms.ModelForm):

    """Form for creating a new fvRsPathAtt object."""
    ap = forms.ModelChoiceField(
        queryset=AciAp.objects.all(),
        to_field_name="name",
        required=False,
    )
    epg = forms.ModelChoiceField(
        queryset=AciEpg.objects.all(),
        to_field_name="name",
        required=False,
    )

    class Meta:
        model = fvRsPathAtt
        fields = [
            "site",
            "encap_id",
            "pod_id",
            "leafs_id",
            "ap",
            "epg",
            "interface",
            "change_ref"

        ]

class fvRsPathAttFilterForm(BootstrapMixin, forms.ModelForm):
    """Form for filtering fvRsPathAtt instances."""

    q = forms.CharField(required=False, label="Search")

    site = forms.ModelChoiceField(
        queryset=Site.objects.all(), required=False, to_field_name="slug"
    )

    device = forms.ModelChoiceField(
        queryset=Device.objects.all(),
        to_field_name="name",
        required=False,
    )

    local_as = forms.IntegerField(
        required=False,
    )

    epg = forms.CharField(
        required=False,
    )

    leafs_id = forms.CharField(
        required=False,
    )
    
    # ap = forms.CharField(
    #     required=False,
    # )
    ap = forms.ModelChoiceField(
        queryset=AciAp.objects.all(),
        to_field_name="name",
        required=False,
    )
    epg = forms.CharField(
        required=False,
    )
    interface = forms.CharField(
        required=False,
    )
    change_ref = forms.CharField(
        required=True,
    )

    class Meta:
        model = fvRsPathAtt
        fields = []

################################ Aci Tenant #########

class AciTenantForm(BootstrapMixin, forms.ModelForm):
    """Form for creating a new fvRsPathAtt object."""

    class Meta:
        model = AciTenant
        fields = [
            "name",
            "description",

        ]

class AciTenantFilterForm(BootstrapMixin, forms.ModelForm):
    """Form for filtering fvRsPathAtt instances."""

    q = forms.CharField(required=False, label="Search")

    # site = forms.ModelChoiceField(
    #     queryset=Site.objects.all(), required=False, to_field_name="slug"
    # )

    # device = forms.ModelChoiceField(
    #     queryset=Device.objects.all(),
    #     to_field_name="name",
    #     required=False,
    # )

    # local_as = forms.IntegerField(
    #     required=False,
    # )

    name = forms.CharField(
        required=False,
    )
    description = forms.CharField(
        required=False,
    )


    class Meta:
        model = AciTenant
        fields = []

################################ Aci Ap #########

class AciApForm(BootstrapMixin, forms.ModelForm):
    """Form for creating a new fvRsPathAtt object."""

    class Meta:
        model = AciAp
        fields = [
            "name",
            "description",

        ]

class AciApFilterForm(BootstrapMixin, forms.ModelForm):
    """Form for filtering fvRsPathAtt instances."""

    q = forms.CharField(required=False, label="Search")

    # site = forms.ModelChoiceField(
    #     queryset=Site.objects.all(), required=False, to_field_name="slug"
    # )

    # device = forms.ModelChoiceField(
    #     queryset=Device.objects.all(),
    #     to_field_name="name",
    #     required=False,
    # )

    # local_as = forms.IntegerField(
    #     required=False,
    # )

    name = forms.CharField(
        required=False,
    )
    description = forms.CharField(
        required=False,
    )


    class Meta:
        model = AciAp
        fields = []

################################ Aci EPG #########

class AciEpgForm(BootstrapMixin, forms.ModelForm):
    """Form for creating a new fvRsPathAtt object."""

    class Meta:
        model = AciEpg
        fields = [
            "name",
            "description",

        ]

class AciEpgFilterForm(BootstrapMixin, forms.ModelForm):
    """Form for filtering fvRsPathAtt instances."""

    q = forms.CharField(required=False, label="Search")

    # site = forms.ModelChoiceField(
    #     queryset=Site.objects.all(), required=False, to_field_name="slug"
    # )

    # device = forms.ModelChoiceField(
    #     queryset=Device.objects.all(),
    #     to_field_name="name",
    #     required=False,
    # )

    # local_as = forms.IntegerField(
    #     required=False,
    # )

    name = forms.CharField(
        required=False,
    )
    description = forms.CharField(
        required=False,
    )


    class Meta:
        model = AciEpg
        fields = []

################################################################

class fvRsPathAttCSVForm(CustomFieldModelCSVForm):
    """Form for entering CSV to bulk-import fvRsPathAtt objects."""
    ap = forms.ModelChoiceField(
        queryset=AciAp.objects.all(),
        to_field_name="name",
        required=True,
    )
    epg = forms.ModelChoiceField(
        queryset=AciEpg.objects.all(),
        to_field_name="name",
        required=True,
    )
    site = forms.ModelChoiceField(
        queryset=Site.objects.all(), required=True, to_field_name="name",
    )
    encap_id = forms.ModelChoiceField(
        queryset=VLAN.objects.all(), required=True, to_field_name="name",
    )

    class Meta:
        model = fvRsPathAtt
        fields = fvRsPathAtt.csv_headers

    def save(self, commit=True, **kwargs):
        """Save the model"""
        model = super().save(commit=commit, **kwargs)
        return model