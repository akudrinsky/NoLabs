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

from nolabs_microservice.models.run_gene_ontology_response import RunGeneOntologyResponse

class TestRunGeneOntologyResponse(unittest.TestCase):
    """RunGeneOntologyResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RunGeneOntologyResponse:
        """Test RunGeneOntologyResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RunGeneOntologyResponse`
        """
        model = RunGeneOntologyResponse()
        if include_optional:
            return RunGeneOntologyResponse(
                experiment_id = None,
                experiment_name = None,
                amino_acids = None
            )
        else:
            return RunGeneOntologyResponse(
                experiment_id = None,
                experiment_name = None,
                amino_acids = None,
        )
        """

    def testRunGeneOntologyResponse(self):
        """Test RunGeneOntologyResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()