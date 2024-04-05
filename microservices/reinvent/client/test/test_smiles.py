# coding: utf-8

"""
    Reinvent4 API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from reinvent_microservice.models.smiles import Smiles

class TestSmiles(unittest.TestCase):
    """Smiles unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Smiles:
        """Test Smiles
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Smiles`
        """
        model = Smiles()
        if include_optional:
            return Smiles(
                smiles = '',
                drug_likeness = 1.337,
                score = 1.337
            )
        else:
            return Smiles(
                smiles = '',
                drug_likeness = 1.337,
                score = 1.337,
        )
        """

    def testSmiles(self):
        """Test Smiles"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
