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

from .linked_service_py3 import LinkedService


class SparkLinkedService(LinkedService):
    """Spark Server linked service.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param connect_via: The integration runtime reference.
    :type connect_via:
     ~azure.mgmt.datafactory.models.IntegrationRuntimeReference
    :param description: Linked service description.
    :type description: str
    :param parameters: Parameters for linked service.
    :type parameters: dict[str,
     ~azure.mgmt.datafactory.models.ParameterSpecification]
    :param annotations: List of tags that can be used for describing the
     Dataset.
    :type annotations: list[object]
    :param type: Required. Constant filled by server.
    :type type: str
    :param host: Required. IP address or host name of the Spark server
    :type host: object
    :param port: Required. The TCP port that the Spark server uses to listen
     for client connections.
    :type port: object
    :param server_type: The type of Spark server. Possible values include:
     'SharkServer', 'SharkServer2', 'SparkThriftServer'
    :type server_type: str or ~azure.mgmt.datafactory.models.SparkServerType
    :param thrift_transport_protocol: The transport protocol to use in the
     Thrift layer. Possible values include: 'Binary', 'SASL', 'HTTP '
    :type thrift_transport_protocol: str or
     ~azure.mgmt.datafactory.models.SparkThriftTransportProtocol
    :param authentication_type: Required. The authentication method used to
     access the Spark server. Possible values include: 'Anonymous', 'Username',
     'UsernameAndPassword', 'WindowsAzureHDInsightService'
    :type authentication_type: str or
     ~azure.mgmt.datafactory.models.SparkAuthenticationType
    :param username: The user name that you use to access Spark Server.
    :type username: object
    :param password: The password corresponding to the user name that you
     provided in the Username field
    :type password: ~azure.mgmt.datafactory.models.SecretBase
    :param http_path: The partial URL corresponding to the Spark server.
    :type http_path: object
    :param enable_ssl: Specifies whether the connections to the server are
     encrypted using SSL. The default value is false.
    :type enable_ssl: object
    :param trusted_cert_path: The full path of the .pem file containing
     trusted CA certificates for verifying the server when connecting over SSL.
     This property can only be set when using SSL on self-hosted IR. The
     default value is the cacerts.pem file installed with the IR.
    :type trusted_cert_path: object
    :param use_system_trust_store: Specifies whether to use a CA certificate
     from the system trust store or from a specified PEM file. The default
     value is false.
    :type use_system_trust_store: object
    :param allow_host_name_cn_mismatch: Specifies whether to require a
     CA-issued SSL certificate name to match the host name of the server when
     connecting over SSL. The default value is false.
    :type allow_host_name_cn_mismatch: object
    :param allow_self_signed_server_cert: Specifies whether to allow
     self-signed certificates from the server. The default value is false.
    :type allow_self_signed_server_cert: object
    :param encrypted_credential: The encrypted credential used for
     authentication. Credentials are encrypted using the integration runtime
     credential manager. Type: string (or Expression with resultType string).
    :type encrypted_credential: object
    """

    _validation = {
        'type': {'required': True},
        'host': {'required': True},
        'port': {'required': True},
        'authentication_type': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'connect_via': {'key': 'connectVia', 'type': 'IntegrationRuntimeReference'},
        'description': {'key': 'description', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': '{ParameterSpecification}'},
        'annotations': {'key': 'annotations', 'type': '[object]'},
        'type': {'key': 'type', 'type': 'str'},
        'host': {'key': 'typeProperties.host', 'type': 'object'},
        'port': {'key': 'typeProperties.port', 'type': 'object'},
        'server_type': {'key': 'typeProperties.serverType', 'type': 'str'},
        'thrift_transport_protocol': {'key': 'typeProperties.thriftTransportProtocol', 'type': 'str'},
        'authentication_type': {'key': 'typeProperties.authenticationType', 'type': 'str'},
        'username': {'key': 'typeProperties.username', 'type': 'object'},
        'password': {'key': 'typeProperties.password', 'type': 'SecretBase'},
        'http_path': {'key': 'typeProperties.httpPath', 'type': 'object'},
        'enable_ssl': {'key': 'typeProperties.enableSsl', 'type': 'object'},
        'trusted_cert_path': {'key': 'typeProperties.trustedCertPath', 'type': 'object'},
        'use_system_trust_store': {'key': 'typeProperties.useSystemTrustStore', 'type': 'object'},
        'allow_host_name_cn_mismatch': {'key': 'typeProperties.allowHostNameCNMismatch', 'type': 'object'},
        'allow_self_signed_server_cert': {'key': 'typeProperties.allowSelfSignedServerCert', 'type': 'object'},
        'encrypted_credential': {'key': 'typeProperties.encryptedCredential', 'type': 'object'},
    }

    def __init__(self, *, host, port, authentication_type, additional_properties=None, connect_via=None, description: str=None, parameters=None, annotations=None, server_type=None, thrift_transport_protocol=None, username=None, password=None, http_path=None, enable_ssl=None, trusted_cert_path=None, use_system_trust_store=None, allow_host_name_cn_mismatch=None, allow_self_signed_server_cert=None, encrypted_credential=None, **kwargs) -> None:
        super(SparkLinkedService, self).__init__(additional_properties=additional_properties, connect_via=connect_via, description=description, parameters=parameters, annotations=annotations, **kwargs)
        self.host = host
        self.port = port
        self.server_type = server_type
        self.thrift_transport_protocol = thrift_transport_protocol
        self.authentication_type = authentication_type
        self.username = username
        self.password = password
        self.http_path = http_path
        self.enable_ssl = enable_ssl
        self.trusted_cert_path = trusted_cert_path
        self.use_system_trust_store = use_system_trust_store
        self.allow_host_name_cn_mismatch = allow_host_name_cn_mismatch
        self.allow_self_signed_server_cert = allow_self_signed_server_cert
        self.encrypted_credential = encrypted_credential
        self.type = 'Spark'
