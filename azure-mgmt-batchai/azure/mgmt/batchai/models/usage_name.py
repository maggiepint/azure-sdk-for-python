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


class UsageName(Model):
    """The Usage Names.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar value: The name of the resource.
    :vartype value: str
    :ivar localized_value: The localized name of the resource.
    :vartype localized_value: str
    """

    _validation = {
        'value': {'readonly': True},
        'localized_value': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'},
        'localized_value': {'key': 'localizedValue', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(UsageName, self).__init__(**kwargs)
        self.value = None
        self.localized_value = None