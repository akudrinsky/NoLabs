__all__ = [
    'BiobuddyDependencies'
]

from typing import Annotated

from fastapi import Depends

from biobuddy_microservice import DefaultApi

from nolabs.refined.application.use_cases.biobuddy.functions.di import FunctionDependencies
from nolabs.refined.application.use_cases.biobuddy.functions.query_chembl import QueryChemblFunction
from nolabs.refined.application.use_cases.biobuddy.use_cases import CheckBioBuddyEnabledFeature, \
    LoadConversationFeature, CreateMessageFeature, EditMessageFeature, SendQueryFeature
from nolabs.refined.infrastructure.di import InfrastructureDependencies


class BiobuddyDependencies:
    @staticmethod
    def check_biobuddy_enabled() -> CheckBioBuddyEnabledFeature:
        return CheckBioBuddyEnabledFeature()


    @staticmethod
    def load_conversation() -> LoadConversationFeature:
        return LoadConversationFeature()

    @staticmethod
    def create_message() -> CreateMessageFeature:
        return CreateMessageFeature()

    @staticmethod
    def edit_message() -> EditMessageFeature:
        return EditMessageFeature()

    @staticmethod
    def send_query(
            biobuddy: Annotated[DefaultApi, Depends(InfrastructureDependencies.biobuddy_microservice)],
            query_chembl: Annotated[QueryChemblFunction, Depends(FunctionDependencies.query_chembl_function)]
    ) -> SendQueryFeature:
        return SendQueryFeature(
            biobuddy_microservice=biobuddy,
            functions=[query_chembl]
        )
