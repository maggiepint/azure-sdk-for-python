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


class StackMajorVersion(Model):
    """Application stack major version.

    :param display_version: Application stack major version (display only).
    :type display_version: str
    :param runtime_version: Application stack major version (runtime only).
    :type runtime_version: str
    :param is_default: <code>true</code> if this is the default major version;
     otherwise, <code>false</code>.
    :type is_default: bool
    :param minor_versions: Minor versions associated with the major version.
    :type minor_versions: list[~azure.mgmt.web.models.StackMinorVersion]
    :param application_insights: <code>true</code> if this supports
     Application Insights; otherwise, <code>false</code>.
    :type application_insights: bool
    """

    _attribute_map = {
        'display_version': {'key': 'displayVersion', 'type': 'str'},
        'runtime_version': {'key': 'runtimeVersion', 'type': 'str'},
        'is_default': {'key': 'isDefault', 'type': 'bool'},
        'minor_versions': {'key': 'minorVersions', 'type': '[StackMinorVersion]'},
        'application_insights': {'key': 'applicationInsights', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(StackMajorVersion, self).__init__(**kwargs)
        self.display_version = kwargs.get('display_version', None)
        self.runtime_version = kwargs.get('runtime_version', None)
        self.is_default = kwargs.get('is_default', None)
        self.minor_versions = kwargs.get('minor_versions', None)
        self.application_insights = kwargs.get('application_insights', None)
