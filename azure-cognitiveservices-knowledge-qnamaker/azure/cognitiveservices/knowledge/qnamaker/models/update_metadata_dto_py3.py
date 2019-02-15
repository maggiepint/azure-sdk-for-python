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


class UpdateMetadataDTO(Model):
    """PATCH Body schema to represent list of Metadata to be updated.

    :param delete: List of Metadata associated with answer to be deleted
    :type delete:
     list[~azure.cognitiveservices.knowledge.qnamaker.models.MetadataDTO]
    :param add: List of metadata associated with answer to be added
    :type add:
     list[~azure.cognitiveservices.knowledge.qnamaker.models.MetadataDTO]
    """

    _attribute_map = {
        'delete': {'key': 'delete', 'type': '[MetadataDTO]'},
        'add': {'key': 'add', 'type': '[MetadataDTO]'},
    }

    def __init__(self, *, delete=None, add=None, **kwargs) -> None:
        super(UpdateMetadataDTO, self).__init__(**kwargs)
        self.delete = delete
        self.add = add
