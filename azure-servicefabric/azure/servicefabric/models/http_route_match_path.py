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

from msrest.serialization import Model


class HttpRouteMatchPath(Model):
    """Path to match for routing.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param value: Required. Uri path to match for request.
    :type value: str
    :param rewrite: replacement string for matched part of the Uri.
    :type rewrite: str
    :ivar type: Required. how to match value in the Uri. Default value:
     "prefix" .
    :vartype type: str
    """

    _validation = {
        'value': {'required': True},
        'type': {'required': True, 'constant': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'},
        'rewrite': {'key': 'rewrite', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    type = "prefix"

    def __init__(self, **kwargs):
        super(HttpRouteMatchPath, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.rewrite = kwargs.get('rewrite', None)
