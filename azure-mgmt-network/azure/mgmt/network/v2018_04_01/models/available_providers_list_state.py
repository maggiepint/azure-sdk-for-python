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


class AvailableProvidersListState(Model):
    """State details.

    :param state_name: The state name.
    :type state_name: str
    :param providers: A list of Internet service providers.
    :type providers: list[str]
    :param cities: List of available cities or towns in the state.
    :type cities:
     list[~azure.mgmt.network.v2018_04_01.models.AvailableProvidersListCity]
    """

    _attribute_map = {
        'state_name': {'key': 'stateName', 'type': 'str'},
        'providers': {'key': 'providers', 'type': '[str]'},
        'cities': {'key': 'cities', 'type': '[AvailableProvidersListCity]'},
    }

    def __init__(self, **kwargs):
        super(AvailableProvidersListState, self).__init__(**kwargs)
        self.state_name = kwargs.get('state_name', None)
        self.providers = kwargs.get('providers', None)
        self.cities = kwargs.get('cities', None)
