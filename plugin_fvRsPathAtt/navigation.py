
from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

from .icon_classes import icon_classes

menu_items = (
    PluginMenuItem(
        link='plugins:plugin_fvRsPathAtt:AciTenant_list',
        link_text='ACI Tenants',
        buttons=(
            PluginMenuButton(
                link="plugins:plugin_fvRsPathAtt:fvRsPathAtt_add",
                title="Add",
                icon_class=icon_classes.get("plus"),
                color=ButtonColorChoices.GREEN,
                permissions=["plugin_fvRsPathAtt.add_fvRsPathAtt"],
            ),
        ),
    ),
    PluginMenuItem(
        link='plugins:plugin_fvRsPathAtt:AciAp_list',
        link_text='ACI Application Profiles',
        buttons=(
            PluginMenuButton(
                link="plugins:plugin_fvRsPathAtt:fvRsPathAtt_add",
                title="Add",
                icon_class=icon_classes.get("plus"),
                color=ButtonColorChoices.GREEN,
                permissions=["plugin_fvRsPathAtt.add_fvRsPathAtt"],
            ),
        ),
    ),
    PluginMenuItem(
        link='plugins:plugin_fvRsPathAtt:AciEpg_list',
        link_text='ACI End Point Groups',
        buttons=(
            PluginMenuButton(
                link="plugins:plugin_fvRsPathAtt:fvRsPathAtt_add",
                title="Add",
                icon_class=icon_classes.get("plus"),
                color=ButtonColorChoices.GREEN,
                permissions=["plugin_fvRsPathAtt.add_fvRsPathAtt"],
            ),
        ),
    ),
    PluginMenuItem(
        link='plugins:plugin_fvRsPathAtt:fvRsPathAtt_list',
        link_text='StaticPath to EPG Objs',
        buttons=(
            PluginMenuButton(
                link="plugins:plugin_fvRsPathAtt:fvRsPathAtt_add",
                title="Add",
                icon_class=icon_classes.get("plus"),
                color=ButtonColorChoices.GREEN,
                permissions=["plugin_fvRsPathAtt.add_fvRsPathAtt"],
            ),
            PluginMenuButton(
                link="plugins:plugin_fvRsPathAtt:fvRsPathAtt_import",
                title="Bulk Add",
                icon_class=icon_classes.get("import"),
                color=ButtonColorChoices.BLUE,
                permissions=["plugin_fvRsPathAtt.add_fvRsPathAtt"],
            ),
        ),
    ),
)
