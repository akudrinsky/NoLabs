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

from nolabs_microservice.models.function_call_return_data import FunctionCallReturnData

class TestFunctionCallReturnData(unittest.TestCase):
    """FunctionCallReturnData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FunctionCallReturnData:
        """Test FunctionCallReturnData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FunctionCallReturnData`
        """
        model = FunctionCallReturnData()
        if include_optional:
            return FunctionCallReturnData(
                files = None
            )
        else:
            return FunctionCallReturnData(
                files = None,
        )
        """

    def testFunctionCallReturnData(self):
        """Test FunctionCallReturnData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
