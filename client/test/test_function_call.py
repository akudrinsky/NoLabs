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

from nolabs_microservice.models.function_call import FunctionCall

class TestFunctionCall(unittest.TestCase):
    """FunctionCall unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FunctionCall:
        """Test FunctionCall
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FunctionCall`
        """
        model = FunctionCall()
        if include_optional:
            return FunctionCall(
                function_name = None,
                parameters = None,
                data = nolabs_microservice.models.function_call_return_data.FunctionCallReturnData(
                    files = null, )
            )
        else:
            return FunctionCall(
                function_name = None,
                parameters = None,
        )
        """

    def testFunctionCall(self):
        """Test FunctionCall"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
