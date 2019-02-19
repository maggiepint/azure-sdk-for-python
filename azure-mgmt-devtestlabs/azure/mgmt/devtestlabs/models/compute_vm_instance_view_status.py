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


class ComputeVmInstanceViewStatus(Model):
    """Status information about a virtual machine.

    :param code: Gets the status Code.
    :type code: str
    :param display_status: Gets the short localizable label for the status.
    :type display_status: str
    :param message: Gets the message associated with the status.
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'display_status': {'key': 'displayStatus', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ComputeVmInstanceViewStatus, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.display_status = kwargs.get('display_status', None)
        self.message = kwargs.get('message', None)
