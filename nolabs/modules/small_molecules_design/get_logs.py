from typing import List

from reinvent_microservice import Configuration, ApiClient, DefaultApi

from nolabs.api_models.small_molecules_design import LogsResponse
from nolabs.modules.small_molecules_design.services.file_management import FileManagement
from nolabs.infrastructure.settings import Settings


class GetLogsFeature:
    def __init__(self, file_management: FileManagement, settings: Settings):
        self._settings = settings
        self._fm = file_management

    async def handle(self, experiment_id: str) -> LogsResponse:
        configuration = Configuration(
            host=self._settings.reinvent_host,
        )
        with ApiClient(configuration=configuration) as client:
            api_instance = DefaultApi(client)

            response = api_instance.logs_jobs_job_id_logs_get(experiment_id)

            if not response:
                return LogsResponse(
                    output='Nothing',
                    docking_output='Nothing',
                    errors='Nothing'
                )

            return LogsResponse(output=response.output,
                                docking_output=response.docking_output,
                                errors=response.errors)
