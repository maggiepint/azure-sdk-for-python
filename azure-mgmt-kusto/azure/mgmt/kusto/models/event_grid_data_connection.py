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

from .data_connection import DataConnection


class EventGridDataConnection(DataConnection):
    """Class representing an Event Grid data connection.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Ex-
     Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
    :vartype type: str
    :param location: Resource location.
    :type location: str
    :param kind: Required. Constant filled by server.
    :type kind: str
    :param storage_account_resource_id: Required. The resource ID of the
     storage account where the data resides.
    :type storage_account_resource_id: str
    :param event_hub_resource_id: Required. The resource ID where the event
     grid is configured to send events.
    :type event_hub_resource_id: str
    :param consumer_group: Required. The event hub consumer group.
    :type consumer_group: str
    :param table_name: Required. The table where the data should be ingested.
     Optionally the table information can be added to each message.
    :type table_name: str
    :param mapping_rule_name: The mapping rule to be used to ingest the data.
     Optionally the mapping information can be added to each message.
    :type mapping_rule_name: str
    :param data_format: Required. The data format of the message. Optionally
     the data format can be added to each message. Possible values include:
     'MULTIJSON', 'JSON', 'CSV', 'TSV', 'SCSV', 'SOHSV', 'PSV', 'TXT', 'RAW',
     'SINGLEJSON', 'AVRO'
    :type data_format: str or ~azure.mgmt.kusto.models.DataFormat
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'kind': {'required': True},
        'storage_account_resource_id': {'required': True},
        'event_hub_resource_id': {'required': True},
        'consumer_group': {'required': True},
        'table_name': {'required': True},
        'data_format': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'storage_account_resource_id': {'key': 'properties.storageAccountResourceId', 'type': 'str'},
        'event_hub_resource_id': {'key': 'properties.eventHubResourceId', 'type': 'str'},
        'consumer_group': {'key': 'properties.consumerGroup', 'type': 'str'},
        'table_name': {'key': 'properties.tableName', 'type': 'str'},
        'mapping_rule_name': {'key': 'properties.mappingRuleName', 'type': 'str'},
        'data_format': {'key': 'properties.dataFormat', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(EventGridDataConnection, self).__init__(**kwargs)
        self.storage_account_resource_id = kwargs.get('storage_account_resource_id', None)
        self.event_hub_resource_id = kwargs.get('event_hub_resource_id', None)
        self.consumer_group = kwargs.get('consumer_group', None)
        self.table_name = kwargs.get('table_name', None)
        self.mapping_rule_name = kwargs.get('mapping_rule_name', None)
        self.data_format = kwargs.get('data_format', None)
        self.kind = 'EventGrid'
