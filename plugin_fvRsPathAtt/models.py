from django.db import models
from django.urls import reverse

from utilities.choices import ChoiceSet
from dcim.fields import ASNField
from extras.models import ChangeLoggedModel
from ipam.fields import IPAddressField
from utilities.querysets import RestrictedQuerySet

'''
This is what needs to be modeled;

- name: Deploy Static Path binding for given EPG
  cisco.aci.aci_static_binding_to_epg:
    host: apic
    username: admin
    password: SomeSecretPassword
    tenant: accessport-code-cert <--------------------------------
    ap: accessport_code_app
    epg: accessport_epg1
    encap_id: 222
    deploy_immediacy: lazy
    interface_mode: untagged
    interface_type: switch_port
    pod_id: 1
    leafs: 101
    interface: '1/7'
    state: present
  delegate_to: localhost

  Any changes to the Model will need the NetBox makemigrations command run to update the database.
  - Update admin.py
  - update views.py
  - create html templates 
  - update tables.py
  - update forms.py
  - update filters.py
  - update urls.py

'''




# @extras_features('export_templates', 'webhooks')


class AciTenant(ChangeLoggedModel):
    """
    """
    name = models.CharField(max_length=64, blank=False,
                            help_text="The ACI Tenant")
    description = models.CharField(
        max_length=200, blank=True, help_text="Write some useful information")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Provide absolute URL to a Tenant Object."""
        return reverse('plugins:plugin_fvRsPathAtt:AciTenant', kwargs={"pk": self.pk})

    objects = RestrictedQuerySet.as_manager()
    # By using RestrictedQuerySet NetBox will be able to filter out objects for which user does not have specific rights #


class AciAp(ChangeLoggedModel):
    """
    """
    name = models.CharField(max_length=64, blank=False,
                            help_text="The ACI Application profile")
    aci_tenant = models.ForeignKey(AciTenant,
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    description = models.CharField(
        max_length=200, blank=True, help_text="Write some useful information")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Provide absolute URL to a Tenant Object."""
        return reverse('plugins:plugin_fvRsPathAtt:AciAp', kwargs={"pk": self.pk})

    objects = RestrictedQuerySet.as_manager()
    # By using RestrictedQuerySet NetBox will be able to filter out objects for which user does not have specific rights #


class AciEpg(ChangeLoggedModel):
    """
    """
    name = models.CharField(max_length=64, blank=False,
                            help_text="The ACI Application profile")
    aci_ap = models.ForeignKey(
        AciAp,
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    description = models.CharField(
        max_length=200, blank=True, help_text="Write some useful information")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Provide absolute URL to a Tenant Object."""
        return reverse('plugins:plugin_fvRsPathAtt:AciEpg', kwargs={"pk": self.pk})

    objects = RestrictedQuerySet.as_manager()
    # By using RestrictedQuerySet NetBox will be able to filter out objects for which user does not have specific rights #


class fvRsPathAtt(ChangeLoggedModel):
    site = models.ForeignKey(
        to="dcim.Site", on_delete=models.SET_NULL, blank=False, null=True
    )
    encap_id = models.ForeignKey(
        to="ipam.VLAN", on_delete=models.SET_NULL, null=True, blank=False)
    pod_id = models.PositiveIntegerField(
        blank=False, help_text="Usually set to 1")
    leafs_id = models.PositiveIntegerField(
        blank=False, help_text="the three digit node id i.e 101 , 102 etc")
    ap = models.CharField(max_length=64, blank=False,
                          help_text="The Application profile name")
    bob = models.ForeignKey(
        AciAp,
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    epg = models.CharField(max_length=64, blank=False,
                           help_text="The EPG name")
    interface = models.CharField(
        max_length=64, blank=False, help_text="The interface id in slot/port format eaxample 1/47")
    change_ref = models.CharField(
        max_length=64, blank=False, help_text="Change reference")

    csv_headers = ["site", "encap_id", "pod_id" , "leafs_id", "ap", "epg" , "interface" , "change_ref"] # fix this

    def __str__(self):
      return f"{self.ap}/{self.epg}"

    def get_absolute_url(self):
        """Provide absolute URL to a fvRsPathAtt Object."""
        return reverse("plugins:plugin_fvRsPathAtt:fvRsPathAtt", kwargs={"pk": self.pk})

    objects = RestrictedQuerySet.as_manager()
    # By using RestrictedQuerySet NetBox will be able to filter out objects for which user does not have specific rights #