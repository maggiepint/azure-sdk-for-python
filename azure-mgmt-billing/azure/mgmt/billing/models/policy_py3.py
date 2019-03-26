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

from .resource_py3 import Resource


class Policy(Resource):
    """The Policy.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param reservation_purchases_allowed: The reservationPurchasesAllowed
     flag.
    :type reservation_purchases_allowed: bool
    :param marketplace_purchases_allowed: The marketplacePurchasesAllowed
     flag.
    :type marketplace_purchases_allowed: bool
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'reservation_purchases_allowed': {'key': 'properties.reservationPurchasesAllowed', 'type': 'bool'},
        'marketplace_purchases_allowed': {'key': 'properties.marketplacePurchasesAllowed', 'type': 'bool'},
    }

    def __init__(self, *, reservation_purchases_allowed: bool=None, marketplace_purchases_allowed: bool=None, **kwargs) -> None:
        super(Policy, self).__init__(**kwargs)
        self.reservation_purchases_allowed = reservation_purchases_allowed
        self.marketplace_purchases_allowed = marketplace_purchases_allowed
