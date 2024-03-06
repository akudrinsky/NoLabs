from typing import Dict, Any

from nolabs.domain.experiment import ExperimentId
from nolabs.features.biobuddy.data_models.message import FunctionCall, FunctionParam
from nolabs.features.biobuddy.functions.base_function import BiobuddyFunction, FunctionParameterDefinition
from nolabs.features.drug_discovery.services.target_file_management import TargetsFileManagement
from nolabs.infrastructure.settings import Settings

import rcsb_pdb_query_microservice
from rcsb_pdb_query_microservice import DefaultApi as rcsbApiDefaultApi
from rcsb_pdb_query_microservice import ApiClient as rcsbApiClient
from rcsb_pdb_query_microservice import Configuration as rcsbApiConfiguration

from nolabs.utils.fasta import create_upload_file_from_string


class QueryRcsbPdbByIdFunction(BiobuddyFunction):
    def __init__(self, settings: Settings,
                 targets_file_management: TargetsFileManagement):
        parameters = [
            FunctionParameterDefinition(name="pdb_ids",
                                        type="array",
                                        required=True,
                                        description="Query RCSB PDB by protein ids. Don't use DNA or RNA ids. If a "
                                                    "user asks for to pull targets/proteins then invoke this method.",
                                        items_type="string")
        ]
        super().__init__("query_rcsb_pdb_by_id", "Query RCSB PDB by protein ids.", parameters)
        self._settings = settings
        self._targets_file_management = targets_file_management

    def execute(self, experiment_id: ExperimentId, arguments: Dict[str, Any]) -> FunctionCall:
        pdb_ids = arguments[self.parameters[0].name]
        print(f"Executing {self.name} with arguments {arguments}")
        configuration = rcsbApiConfiguration(
            host=self._settings.rcsb_pdb_query_host,
        )
        with rcsbApiClient(configuration=configuration) as client:
            api_instance = rcsbApiDefaultApi(client)
            request = rcsb_pdb_query_microservice.GetFastaFilesByIdsRequest(rcsb_pdb_ids=pdb_ids)
            response = api_instance.fetch_fetch_fastas_by_ids_post(get_fasta_files_by_ids_request=request)

            results = [(result.fasta_contents, result.link) for result in response.fasta_contents]

            reply_content = f"Sure! Pulled some targets, check them out: \n"
            for result in results:
                reply_content += f'{result[1]} \n'
            for result in results:
                temp_res = result[0][:]
                file = create_upload_file_from_string(temp_res, "protein.fasta")
                additional_metadata = {
                    "link": result[1]
                }
                self._targets_file_management.store_target(experiment_id, file, additional_metadata)

            return FunctionCall(function_name="query_rcsb_pdb_by_id", parameters=[FunctionParam(name="pdb_ids",
                                                                                                value=pdb_ids)])
