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


class InformationalUrl(Model):
    """Represents a group of URIs that provide terms of service, marketing,
    support and privacy policy information about an application. The default
    value for each string is null.

    :param terms_of_service: The terms of service URI
    :type terms_of_service: str
    :param marketing: The marketing URI
    :type marketing: str
    :param privacy: The privacy policy URI
    :type privacy: str
    :param support: The support URI
    :type support: str
    """

    _attribute_map = {
        'terms_of_service': {'key': 'termsOfService', 'type': 'str'},
        'marketing': {'key': 'marketing', 'type': 'str'},
        'privacy': {'key': 'privacy', 'type': 'str'},
        'support': {'key': 'support', 'type': 'str'},
    }

    def __init__(self, *, terms_of_service: str=None, marketing: str=None, privacy: str=None, support: str=None, **kwargs) -> None:
        super(InformationalUrl, self).__init__(**kwargs)
        self.terms_of_service = terms_of_service
        self.marketing = marketing
        self.privacy = privacy
        self.support = support
