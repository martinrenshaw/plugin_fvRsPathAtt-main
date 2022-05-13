# Netbox Pluginfvrspathatt
[Netbox](https://github.com/netbox-community/netbox) Plugin description

This plugin was design so that I could use Ansible module Cisco.aci.aci.static_binding_to _epg (fv:RsPathAtt) abd fetch the info from Netbox API.
We found that this process manually was time-consuming.

## Compatibility

This plugin in compatible with [NetBox](https://netbox.readthedocs.org/) 2.10 and later.

## Installation

The plugin is available as a Python package in pypi and can be installed with pip

```
pip install netbox-plugin-fvRsPathAtt
```
Enable the plugin in /opt/netbox/netbox/netbox/configuration.py:
```
PLUGINS = ['plugin_fvRsPathAtt']
```

## Configuration

## Screenshots
