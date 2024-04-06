from fastapi import FastAPI
from diffdock.services import run_docking
from diffdock.api_models import RunDiffDockPredictionRequest, RunDiffDockPredictionResponse, IsJobRunningResponse

app = FastAPI(
    title="Diff Dock"
)

from diffdock.job_state_manager import job_state_manager
from malevich.square import processor


@processor()
@app.post("/run-docking")
def predict(request: RunDiffDockPredictionRequest) -> RunDiffDockPredictionResponse:
    if request.job_id:
        job_state_manager.start_job(request.job_id)
    result = run_docking(request)
    if request.job_id:
        job_state_manager.finish_job(request.job_id)
    return result


@processor()
@app.get("/job/{job_id}/is-running")
def is_job_running(job_id: str) -> IsJobRunningResponse:
    return IsJobRunningResponse(is_running=job_state_manager.is_job_running(job_id))


@processor()
@app.get("/jobs/running")
def get_running_jobs():
    return {"running_jobs": job_state_manager.get_running_jobs()}
