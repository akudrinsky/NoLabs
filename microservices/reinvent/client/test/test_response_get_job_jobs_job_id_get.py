# coding: utf-8

"""
    Reinvent4 API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from reinvent_microservice.models.response_get_job_jobs_job_id_get import ResponseGetJobJobsJobIdGet

class TestResponseGetJobJobsJobIdGet(unittest.TestCase):
    """ResponseGetJobJobsJobIdGet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResponseGetJobJobsJobIdGet:
        """Test ResponseGetJobJobsJobIdGet
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResponseGetJobJobsJobIdGet`
        """
        model = ResponseGetJobJobsJobIdGet()
        if include_optional:
            return ResponseGetJobJobsJobIdGet(
                id = None,
                name = None,
                created_at = None,
                running = None,
                learning_completed = None
            )
        else:
            return ResponseGetJobJobsJobIdGet(
                id = None,
                name = None,
                created_at = None,
                running = None,
                learning_completed = None,
        )
        """

    def testResponseGetJobJobsJobIdGet(self):
        """Test ResponseGetJobJobsJobIdGet"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
