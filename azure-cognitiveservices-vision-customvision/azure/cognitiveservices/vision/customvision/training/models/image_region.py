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


class ImageRegion(Model):
    """ImageRegion.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar region_id:
    :vartype region_id: str
    :ivar tag_name:
    :vartype tag_name: str
    :ivar created:
    :vartype created: datetime
    :param tag_id: Id of the tag associated with this region.
    :type tag_id: str
    :param left:
    :type left: float
    :param top:
    :type top: float
    :param width:
    :type width: float
    :param height:
    :type height: float
    """

    _validation = {
        'region_id': {'readonly': True},
        'tag_name': {'readonly': True},
        'created': {'readonly': True},
    }

    _attribute_map = {
        'region_id': {'key': 'regionId', 'type': 'str'},
        'tag_name': {'key': 'tagName', 'type': 'str'},
        'created': {'key': 'created', 'type': 'iso-8601'},
        'tag_id': {'key': 'tagId', 'type': 'str'},
        'left': {'key': 'left', 'type': 'float'},
        'top': {'key': 'top', 'type': 'float'},
        'width': {'key': 'width', 'type': 'float'},
        'height': {'key': 'height', 'type': 'float'},
    }

    def __init__(self, **kwargs):
        super(ImageRegion, self).__init__(**kwargs)
        self.region_id = None
        self.tag_name = None
        self.created = None
        self.tag_id = kwargs.get('tag_id', None)
        self.left = kwargs.get('left', None)
        self.top = kwargs.get('top', None)
        self.width = kwargs.get('width', None)
        self.height = kwargs.get('height', None)
