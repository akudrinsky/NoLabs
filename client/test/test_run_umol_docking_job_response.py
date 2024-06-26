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

from nolabs_microservice.models.run_umol_docking_job_response import RunUmolDockingJobResponse

class TestRunUmolDockingJobResponse(unittest.TestCase):
    """RunUmolDockingJobResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RunUmolDockingJobResponse:
        """Test RunUmolDockingJobResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RunUmolDockingJobResponse`
        """
        model = RunUmolDockingJobResponse()
        if include_optional:
            return RunUmolDockingJobResponse(
                predicted_pdb = None,
                predicted_sdf = None,
                plddt_array = None,
                job_id = None
            )
        else:
            return RunUmolDockingJobResponse(
                predicted_pdb = None,
                predicted_sdf = None,
                plddt_array = None,
                job_id = None,
        )
        """

    def testRunUmolDockingJobResponse(self):
        """Test RunUmolDockingJobResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
