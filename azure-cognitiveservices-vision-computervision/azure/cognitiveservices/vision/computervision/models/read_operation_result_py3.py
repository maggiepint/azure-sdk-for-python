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


class ReadOperationResult(Model):
    """OCR result of the read operation.

    :param status: Status of the read operation. Possible values include: 'Not
     Started', 'Running', 'Failed', 'Succeeded'
    :type status: str or
     ~azure.cognitiveservices.vision.computervision.models.TextOperationStatusCodes
    :param recognition_results: A array of text recognition result of the read
     operation.
    :type recognition_results:
     list[~azure.cognitiveservices.vision.computervision.models.TextRecognitionResult]
    """

    _attribute_map = {
        'status': {'key': 'status', 'type': 'TextOperationStatusCodes'},
        'recognition_results': {'key': 'recognitionResults', 'type': '[TextRecognitionResult]'},
    }

    def __init__(self, *, status=None, recognition_results=None, **kwargs) -> None:
        super(ReadOperationResult, self).__init__(**kwargs)
        self.status = status
        self.recognition_results = recognition_results
