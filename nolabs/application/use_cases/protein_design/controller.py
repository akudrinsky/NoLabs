__all__ = [
    'router',
]

from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends

from nolabs.application.use_cases.protein_design.api_models import SetupJobRequest, JobResponse, GetJobStatusResponse
from nolabs.application.use_cases.protein_design.di import ProteinDesignDependencies
from nolabs.application.use_cases.protein_design.use_cases import RunJobFeature, GetJobFeature, SetupJobFeature, \
    GetJobStatusFeature

router = APIRouter(
    prefix='/api/v1/protein-design',
    tags=['Protein design'],

)


@router.post('/jobs/run/{job_id}')
async def run_job(
        feature: Annotated[RunJobFeature, Depends(ProteinDesignDependencies.run_job)],
        job_id: UUID
) -> JobResponse:
    return await feature.handle(job_id=job_id)


@router.get('/jobs/{job_id}',
            summary='Get job')
async def get_job(job_id: UUID, feature: Annotated[
    GetJobFeature, Depends(ProteinDesignDependencies.get_job)]) -> JobResponse:
    return await feature.handle(job_id=job_id)


@router.post('/jobs',
            summary='Setup job')
async def setup_job(request: SetupJobRequest, feature: Annotated[
    SetupJobFeature, Depends(ProteinDesignDependencies.setup_job)]) -> JobResponse:
    return await feature.handle(request=request)


@router.get('/jobs/{job_id}/status',
            summary='Get job execution status')
async def get_job_status(job_id: UUID, feature: Annotated[
    GetJobStatusFeature, Depends(ProteinDesignDependencies.get_job_status)]) -> GetJobStatusResponse:
    return await feature.handle(job_id=job_id)