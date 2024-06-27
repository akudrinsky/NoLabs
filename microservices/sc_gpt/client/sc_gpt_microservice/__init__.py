# coding: utf-8

# flake8: noqa

"""
    SC-GPT API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from sc_gpt_microservice.api.default_api import DefaultApi

# import ApiClient
from sc_gpt_microservice.api_response import ApiResponse
from sc_gpt_microservice.api_client import ApiClient
from sc_gpt_microservice.configuration import Configuration
from sc_gpt_microservice.exceptions import OpenApiException
from sc_gpt_microservice.exceptions import ApiTypeError
from sc_gpt_microservice.exceptions import ApiValueError
from sc_gpt_microservice.exceptions import ApiKeyError
from sc_gpt_microservice.exceptions import ApiAttributeError
from sc_gpt_microservice.exceptions import ApiException

# import models into sdk package
from sc_gpt_microservice.models.embed_request import EmbedRequest
from sc_gpt_microservice.models.embed_response import EmbedResponse
from sc_gpt_microservice.models.http_validation_error import HTTPValidationError
from sc_gpt_microservice.models.reference_mapping_request import ReferenceMappingRequest
from sc_gpt_microservice.models.reference_mapping_response import ReferenceMappingResponse
from sc_gpt_microservice.models.validation_error import ValidationError
from sc_gpt_microservice.models.validation_error_loc_inner import ValidationErrorLocInner