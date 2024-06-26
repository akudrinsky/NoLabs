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

from nolabs_microservice.models.nolabs_api_models_protein_design_experiment_properties_response import NolabsApiModelsProteinDesignExperimentPropertiesResponse

class TestNolabsApiModelsProteinDesignExperimentPropertiesResponse(unittest.TestCase):
    """NolabsApiModelsProteinDesignExperimentPropertiesResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NolabsApiModelsProteinDesignExperimentPropertiesResponse:
        """Test NolabsApiModelsProteinDesignExperimentPropertiesResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NolabsApiModelsProteinDesignExperimentPropertiesResponse`
        """
        model = NolabsApiModelsProteinDesignExperimentPropertiesResponse()
        if include_optional:
            return NolabsApiModelsProteinDesignExperimentPropertiesResponse(
                pdb_file = None,
                pdb_file_name = None,
                contig = None,
                number_of_designs = None,
                hotspots = None,
                timesteps = None
            )
        else:
            return NolabsApiModelsProteinDesignExperimentPropertiesResponse(
                pdb_file = None,
                pdb_file_name = None,
                contig = None,
                number_of_designs = None,
        )
        """

    def testNolabsApiModelsProteinDesignExperimentPropertiesResponse(self):
        """Test NolabsApiModelsProteinDesignExperimentPropertiesResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
