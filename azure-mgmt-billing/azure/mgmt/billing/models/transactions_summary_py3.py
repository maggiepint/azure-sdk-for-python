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


class TransactionsSummary(Resource):
    """A reservation transaction summary resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param kind: The kind of transaction. Choices are all and reservation.
     Possible values include: 'all', 'reservation'
    :type kind: str or ~azure.mgmt.billing.models.TransactionTypeKind
    :ivar date_property: The date of reservation transaction.
    :vartype date_property: datetime
    :ivar invoice: Invoice number or 'pending' if not invoiced.
    :vartype invoice: str
    :ivar order_id: The reservation order id.
    :vartype order_id: str
    :ivar order_name: The reservation order name.
    :vartype order_name: str
    :ivar product_type_id: The product type id.
    :vartype product_type_id: str
    :ivar product_type: The type of product.
    :vartype product_type: str
    :ivar product_description: Product description.
    :vartype product_description: str
    :param transaction_type: Transaction types. Possible values include:
     'Purchase', 'Usage Charge'
    :type transaction_type: str or ~azure.mgmt.billing.models.ReservationType
    :ivar transaction_amount: Last charge associated with the purchase.
    :vartype transaction_amount: ~azure.mgmt.billing.models.Amount
    :ivar quantity: Purchase quantity.
    :vartype quantity: int
    :ivar invoice_section_id: Invoice section id to which this product
     belongs.
    :vartype invoice_section_id: str
    :ivar invoice_section_name: Invoice section name to which this product
     belongs.
    :vartype invoice_section_name: str
    :ivar billing_profile_id: Billing Profile id to which this product
     belongs.
    :vartype billing_profile_id: str
    :ivar billing_profile_name: Billing Profile name to which this product
     belongs.
    :vartype billing_profile_name: str
    :ivar subscription_id: The subscription id.
    :vartype subscription_id: str
    :ivar subscription_name: The subscription name.
    :vartype subscription_name: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'date_property': {'readonly': True},
        'invoice': {'readonly': True},
        'order_id': {'readonly': True},
        'order_name': {'readonly': True},
        'product_type_id': {'readonly': True},
        'product_type': {'readonly': True},
        'product_description': {'readonly': True},
        'transaction_amount': {'readonly': True},
        'quantity': {'readonly': True},
        'invoice_section_id': {'readonly': True},
        'invoice_section_name': {'readonly': True},
        'billing_profile_id': {'readonly': True},
        'billing_profile_name': {'readonly': True},
        'subscription_id': {'readonly': True},
        'subscription_name': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'kind': {'key': 'properties.kind', 'type': 'str'},
        'date_property': {'key': 'properties.date', 'type': 'iso-8601'},
        'invoice': {'key': 'properties.invoice', 'type': 'str'},
        'order_id': {'key': 'properties.orderId', 'type': 'str'},
        'order_name': {'key': 'properties.orderName', 'type': 'str'},
        'product_type_id': {'key': 'properties.productTypeId', 'type': 'str'},
        'product_type': {'key': 'properties.productType', 'type': 'str'},
        'product_description': {'key': 'properties.productDescription', 'type': 'str'},
        'transaction_type': {'key': 'properties.transactionType', 'type': 'str'},
        'transaction_amount': {'key': 'properties.transactionAmount', 'type': 'Amount'},
        'quantity': {'key': 'properties.quantity', 'type': 'int'},
        'invoice_section_id': {'key': 'properties.invoiceSectionId', 'type': 'str'},
        'invoice_section_name': {'key': 'properties.invoiceSectionName', 'type': 'str'},
        'billing_profile_id': {'key': 'properties.billingProfileId', 'type': 'str'},
        'billing_profile_name': {'key': 'properties.billingProfileName', 'type': 'str'},
        'subscription_id': {'key': 'properties.subscriptionId', 'type': 'str'},
        'subscription_name': {'key': 'properties.subscriptionName', 'type': 'str'},
    }

    def __init__(self, *, kind=None, transaction_type=None, **kwargs) -> None:
        super(TransactionsSummary, self).__init__(**kwargs)
        self.kind = kind
        self.date_property = None
        self.invoice = None
        self.order_id = None
        self.order_name = None
        self.product_type_id = None
        self.product_type = None
        self.product_description = None
        self.transaction_type = transaction_type
        self.transaction_amount = None
        self.quantity = None
        self.invoice_section_id = None
        self.invoice_section_name = None
        self.billing_profile_id = None
        self.billing_profile_name = None
        self.subscription_id = None
        self.subscription_name = None
