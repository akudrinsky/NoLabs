# coding: utf-8

"""
    NoLabs

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from nolabs_microservice.models.get_folding_response import GetFoldingResponse

class TestGetFoldingResponse(unittest.TestCase):
    """GetFoldingResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetFoldingResponse:
        """Test GetFoldingResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetFoldingResponse`
        """
        model = GetFoldingResponse()
        if include_optional:
            return GetFoldingResponse(
                pdb_contents = None
            )
        else:
            return GetFoldingResponse(
                pdb_contents = None,
        )
        """

    def testGetFoldingResponse(self):
        """Test GetFoldingResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
