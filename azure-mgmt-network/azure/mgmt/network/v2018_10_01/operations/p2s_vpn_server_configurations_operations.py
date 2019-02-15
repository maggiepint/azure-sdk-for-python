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

import uuid
from msrest.pipeline import ClientRawResponse
from msrest.polling import LROPoller, NoPolling
from msrestazure.polling.arm_polling import ARMPolling

from .. import models


class P2sVpnServerConfigurationsOperations(object):
    """P2sVpnServerConfigurationsOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: Client API version. Constant value: "2018-10-01".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2018-10-01"

        self.config = config

    def get(
            self, resource_group_name, virtual_wan_name, p2_svpn_server_configuration_name, custom_headers=None, raw=False, **operation_config):
        """Retrieves the details of a P2SVpnServerConfiguration.

        :param resource_group_name: The resource group name of the
         P2SVpnServerConfiguration.
        :type resource_group_name: str
        :param virtual_wan_name: The name of the VirtualWan.
        :type virtual_wan_name: str
        :param p2_svpn_server_configuration_name: The name of the
         P2SVpnServerConfiguration.
        :type p2_svpn_server_configuration_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: P2SVpnServerConfiguration or ClientRawResponse if raw=true
        :rtype:
         ~azure.mgmt.network.v2018_10_01.models.P2SVpnServerConfiguration or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<azure.mgmt.network.v2018_10_01.models.ErrorException>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'virtualWanName': self._serialize.url("virtual_wan_name", virtual_wan_name, 'str'),
            'p2SVpnServerConfigurationName': self._serialize.url("p2_svpn_server_configuration_name", p2_svpn_server_configuration_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('P2SVpnServerConfiguration', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualWans/{virtualWanName}/p2sVpnServerConfigurations/{p2SVpnServerConfigurationName}'}


    def _create_or_update_initial(
            self, resource_group_name, virtual_wan_name, p2_svpn_server_configuration_name, p2_svpn_server_configuration_parameters, custom_headers=None, raw=False, **operation_config):
        # Construct URL
        url = self.create_or_update.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'virtualWanName': self._serialize.url("virtual_wan_name", virtual_wan_name, 'str'),
            'p2SVpnServerConfigurationName': self._serialize.url("p2_svpn_server_configuration_name", p2_svpn_server_configuration_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(p2_svpn_server_configuration_parameters, 'P2SVpnServerConfiguration')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 201]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('P2SVpnServerConfiguration', response)
        if response.status_code == 201:
            deserialized = self._deserialize('P2SVpnServerConfiguration', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def create_or_update(
            self, resource_group_name, virtual_wan_name, p2_svpn_server_configuration_name, p2_svpn_server_configuration_parameters, custom_headers=None, raw=False, polling=True, **operation_config):
        """Creates a P2SVpnServerConfiguration to associate with a VirtualWan if
        it doesn't exist else updates the existing P2SVpnServerConfiguration.

        :param resource_group_name: The resource group name of the VirtualWan.
        :type resource_group_name: str
        :param virtual_wan_name: The name of the VirtualWan.
        :type virtual_wan_name: str
        :param p2_svpn_server_configuration_name: The name of the
         P2SVpnServerConfiguration.
        :type p2_svpn_server_configuration_name: str
        :param p2_svpn_server_configuration_parameters: Parameters supplied to
         create or Update a P2SVpnServerConfiguration.
        :type p2_svpn_server_configuration_parameters:
         ~azure.mgmt.network.v2018_10_01.models.P2SVpnServerConfiguration
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: The poller return type is ClientRawResponse, the
         direct response alongside the deserialized response
        :param polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of LROPoller that returns
         P2SVpnServerConfiguration or
         ClientRawResponse<P2SVpnServerConfiguration> if raw==True
        :rtype:
         ~msrestazure.azure_operation.AzureOperationPoller[~azure.mgmt.network.v2018_10_01.models.P2SVpnServerConfiguration]
         or
         ~msrestazure.azure_operation.AzureOperationPoller[~msrest.pipeline.ClientRawResponse[~azure.mgmt.network.v2018_10_01.models.P2SVpnServerConfiguration]]
        :raises:
         :class:`ErrorException<azure.mgmt.network.v2018_10_01.models.ErrorException>`
        """
        raw_result = self._create_or_update_initial(
            resource_group_name=resource_group_name,
            virtual_wan_name=virtual_wan_name,
            p2_svpn_server_configuration_name=p2_svpn_server_configuration_name,
            p2_svpn_server_configuration_parameters=p2_svpn_server_configuration_parameters,
            custom_headers=custom_headers,
            raw=True,
            **operation_config
        )

        def get_long_running_output(response):
            deserialized = self._deserialize('P2SVpnServerConfiguration', response)

            if raw:
                client_raw_response = ClientRawResponse(deserialized, response)
                return client_raw_response

            return deserialized

        lro_delay = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        if polling is True: polling_method = ARMPolling(lro_delay, **operation_config)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualWans/{virtualWanName}/p2sVpnServerConfigurations/{p2SVpnServerConfigurationName}'}


    def _delete_initial(
            self, resource_group_name, virtual_wan_name, p2_svpn_server_configuration_name, custom_headers=None, raw=False, **operation_config):
        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'virtualWanName': self._serialize.url("virtual_wan_name", virtual_wan_name, 'str'),
            'p2SVpnServerConfigurationName': self._serialize.url("p2_svpn_server_configuration_name", p2_svpn_server_configuration_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 202, 204]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    def delete(
            self, resource_group_name, virtual_wan_name, p2_svpn_server_configuration_name, custom_headers=None, raw=False, polling=True, **operation_config):
        """Deletes a P2SVpnServerConfiguration.

        :param resource_group_name: The resource group name of the
         P2SVpnServerConfiguration.
        :type resource_group_name: str
        :param virtual_wan_name: The name of the VirtualWan.
        :type virtual_wan_name: str
        :param p2_svpn_server_configuration_name: The name of the
         P2SVpnServerConfiguration.
        :type p2_svpn_server_configuration_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: The poller return type is ClientRawResponse, the
         direct response alongside the deserialized response
        :param polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of LROPoller that returns None or
         ClientRawResponse<None> if raw==True
        :rtype: ~msrestazure.azure_operation.AzureOperationPoller[None] or
         ~msrestazure.azure_operation.AzureOperationPoller[~msrest.pipeline.ClientRawResponse[None]]
        :raises:
         :class:`ErrorException<azure.mgmt.network.v2018_10_01.models.ErrorException>`
        """
        raw_result = self._delete_initial(
            resource_group_name=resource_group_name,
            virtual_wan_name=virtual_wan_name,
            p2_svpn_server_configuration_name=p2_svpn_server_configuration_name,
            custom_headers=custom_headers,
            raw=True,
            **operation_config
        )

        def get_long_running_output(response):
            if raw:
                client_raw_response = ClientRawResponse(None, response)
                return client_raw_response

        lro_delay = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        if polling is True: polling_method = ARMPolling(lro_delay, **operation_config)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualWans/{virtualWanName}/p2sVpnServerConfigurations/{p2SVpnServerConfigurationName}'}

    def list_by_virtual_wan(
            self, resource_group_name, virtual_wan_name, custom_headers=None, raw=False, **operation_config):
        """Retrieves all P2SVpnServerConfigurations for a particular VirtualWan.

        :param resource_group_name: The resource group name of the VirtualWan.
        :type resource_group_name: str
        :param virtual_wan_name: The name of the VirtualWan.
        :type virtual_wan_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of P2SVpnServerConfiguration
        :rtype:
         ~azure.mgmt.network.v2018_10_01.models.P2SVpnServerConfigurationPaged[~azure.mgmt.network.v2018_10_01.models.P2SVpnServerConfiguration]
        :raises:
         :class:`ErrorException<azure.mgmt.network.v2018_10_01.models.ErrorException>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = self.list_by_virtual_wan.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'virtualWanName': self._serialize.url("virtual_wan_name", virtual_wan_name, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                raise models.ErrorException(self._deserialize, response)

            return response

        # Deserialize response
        deserialized = models.P2SVpnServerConfigurationPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.P2SVpnServerConfigurationPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized
    list_by_virtual_wan.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualWans/{virtualWanName}/p2sVpnServerConfigurations'}
