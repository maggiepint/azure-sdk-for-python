# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .proxy_only_resource import ProxyOnlyResource


class StorageMigrationOptions(ProxyOnlyResource):
    """Options for app content migration.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource Name.
    :vartype name: str
    :param kind: Kind of resource.
    :type kind: str
    :ivar type: Resource type.
    :vartype type: str
    :param azurefiles_connection_string: Required. AzureFiles connection
     string.
    :type azurefiles_connection_string: str
    :param azurefiles_share: Required. AzureFiles share.
    :type azurefiles_share: str
    :param switch_site_after_migration: <code>true</code>if the app should be
     switched over; otherwise, <code>false</code>. Default value: False .
    :type switch_site_after_migration: bool
    :param block_write_access_to_site: <code>true</code> if the app should be
     read only during copy operation; otherwise, <code>false</code>. Default
     value: False .
    :type block_write_access_to_site: bool
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'azurefiles_connection_string': {'required': True},
        'azurefiles_share': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'azurefiles_connection_string': {'key': 'properties.azurefilesConnectionString', 'type': 'str'},
        'azurefiles_share': {'key': 'properties.azurefilesShare', 'type': 'str'},
        'switch_site_after_migration': {'key': 'properties.switchSiteAfterMigration', 'type': 'bool'},
        'block_write_access_to_site': {'key': 'properties.blockWriteAccessToSite', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(StorageMigrationOptions, self).__init__(**kwargs)
        self.azurefiles_connection_string = kwargs.get('azurefiles_connection_string', None)
        self.azurefiles_share = kwargs.get('azurefiles_share', None)
        self.switch_site_after_migration = kwargs.get('switch_site_after_migration', False)
        self.block_write_access_to_site = kwargs.get('block_write_access_to_site', False)
