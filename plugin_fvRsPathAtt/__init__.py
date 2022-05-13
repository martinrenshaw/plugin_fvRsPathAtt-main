from extras.plugins import PluginConfig
from .version import __version__


class PluginfvrspathattConfig(PluginConfig):
    name = 'plugin_fvRsPathAtt'
    verbose_name = 'Cisco ACI Modeled Objects' # This will be used as the plugin title in the navigation dropdown.
    description = 'Model Cisco ACI fv:RsPathAtt class'
    version = __version__
    author = 'Martin Renshaw'
    author_email = 'martin@martinrenshaw.com'
    base_url = "aci-objects" # This is used as the api base url
    required_settings = []
    default_settings = {}


config = PluginfvrspathattConfig # noqa
