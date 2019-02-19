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

from .run_command_document_base import RunCommandDocumentBase


class RunCommandDocument(RunCommandDocumentBase):
    """Describes the properties of a Run Command.

    All required parameters must be populated in order to send to Azure.

    :param schema: Required. The VM run command schema.
    :type schema: str
    :param id: Required. The VM run command id.
    :type id: str
    :param os_type: Required. The Operating System type. Possible values
     include: 'Windows', 'Linux'
    :type os_type: str or
     ~azure.mgmt.compute.v2018_10_01.models.OperatingSystemTypes
    :param label: Required. The VM run command label.
    :type label: str
    :param description: Required. The VM run command description.
    :type description: str
    :param script: Required. The script to be executed.
    :type script: list[str]
    :param parameters: The parameters used by the script.
    :type parameters:
     list[~azure.mgmt.compute.v2018_10_01.models.RunCommandParameterDefinition]
    """

    _validation = {
        'schema': {'required': True},
        'id': {'required': True},
        'os_type': {'required': True},
        'label': {'required': True},
        'description': {'required': True},
        'script': {'required': True},
    }

    _attribute_map = {
        'schema': {'key': '$schema', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'os_type': {'key': 'osType', 'type': 'OperatingSystemTypes'},
        'label': {'key': 'label', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'script': {'key': 'script', 'type': '[str]'},
        'parameters': {'key': 'parameters', 'type': '[RunCommandParameterDefinition]'},
    }

    def __init__(self, **kwargs):
        super(RunCommandDocument, self).__init__(**kwargs)
        self.script = kwargs.get('script', None)
        self.parameters = kwargs.get('parameters', None)
