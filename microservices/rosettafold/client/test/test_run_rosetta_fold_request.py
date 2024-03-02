# coding: utf-8

"""
    RoseTTAFold API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from rosettafold_microservice.models.run_rosetta_fold_request import RunRosettaFoldRequest

class TestRunRosettaFoldRequest(unittest.TestCase):
    """RunRosettaFoldRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RunRosettaFoldRequest:
        """Test RunRosettaFoldRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RunRosettaFoldRequest`
        """
        model = RunRosettaFoldRequest()
        if include_optional:
            return RunRosettaFoldRequest(
                fasta_content = None,
                a3m_content = None
            )
        else:
            return RunRosettaFoldRequest(
                fasta_content = None,
                a3m_content = None,
        )
        """

    def testRunRosettaFoldRequest(self):
        """Test RunRosettaFoldRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
