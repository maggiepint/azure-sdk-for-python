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

from .log_analytics_input_base import LogAnalyticsInputBase


class ThrottledRequestsInput(LogAnalyticsInputBase):
    """Api request input for LogAnalytics getThrottledRequests Api.

    All required parameters must be populated in order to send to Azure.

    :param blob_container_sas_uri: Required. SAS Uri of the logging blob
     container to which LogAnalytics Api writes output logs to.
    :type blob_container_sas_uri: str
    :param from_time: Required. From time of the query
    :type from_time: datetime
    :param to_time: Required. To time of the query
    :type to_time: datetime
    :param group_by_throttle_policy: Group query result by Throttle Policy
     applied.
    :type group_by_throttle_policy: bool
    :param group_by_operation_name: Group query result by Operation Name.
    :type group_by_operation_name: bool
    :param group_by_resource_name: Group query result by Resource Name.
    :type group_by_resource_name: bool
    """

    _validation = {
        'blob_container_sas_uri': {'required': True},
        'from_time': {'required': True},
        'to_time': {'required': True},
    }

    _attribute_map = {
        'blob_container_sas_uri': {'key': 'blobContainerSasUri', 'type': 'str'},
        'from_time': {'key': 'fromTime', 'type': 'iso-8601'},
        'to_time': {'key': 'toTime', 'type': 'iso-8601'},
        'group_by_throttle_policy': {'key': 'groupByThrottlePolicy', 'type': 'bool'},
        'group_by_operation_name': {'key': 'groupByOperationName', 'type': 'bool'},
        'group_by_resource_name': {'key': 'groupByResourceName', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(ThrottledRequestsInput, self).__init__(**kwargs)
