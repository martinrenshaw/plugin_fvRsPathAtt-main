from rest_framework import serializers

from ipam.api.nested_serializers import (
    NestedIPAddressSerializer, NestedVLANSerializer
)
from dcim.api.nested_serializers import NestedDeviceSerializer, NestedSiteSerializer

from plugin_fvRsPathAtt.models import fvRsPathAtt


class fvRsPathAttSerializer(serializers.ModelSerializer):
    """Serializer for the fvRsPathAtt model."""

    site = NestedSiteSerializer(
        many=False,
        read_only=False,
        required=False,
        help_text="Site x",
    )
    encap_id = NestedVLANSerializer(
        many=False,
        read_only=False,
        help_text="Encap ID",
    )

    # device = NestedDeviceSerializer(
    #     many=False,
    #     read_only=False,
    #     required=True,
    #     help_text="Device",
    # )

    # local_ip = NestedIPAddressSerializer(
    #     many=False,
    #     read_only=False,
    #     required=True,
    #     help_text="Local fvRsPathAtt IP",
    # )

    class Meta:
        model = fvRsPathAtt
        fields = [
            "id",
            "site",
            "encap_id",
            "pod_id",
            "leafs_id",
            "ap",
            "epg",
            "interface",
            "change_ref"
        ]