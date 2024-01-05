import dataclasses
from enum import Enum
from typing import Annotated

from fastapi import UploadFile


class Integrators(Enum):
    langevin = 'LangevinIntegator'
    langevin_middle = 'LangevinMiddleIntegator'
    nose_hoover = 'NoseHooverIntegrator'
    brownian = 'BrownianIntegrator'
    variable_verlet = 'VariableVerletIntegrator'


@dataclasses.dataclass(kw_only=True)
class RunSimulationsRequest:
    pdbFile: UploadFile
    experimentName: str
    experimentId: str
    totalFrames: int = 10000
    temperatureK: float = 273.15
    takeFrameEvery: int = 1000
    stepSize: float = 0.002
    replaceNonStandardResidues: bool = False
    addMissingAtoms: bool = False
    addMissingHydrogens: bool = True
    frictionCoeff: float = 1.0
    ignoreMissingAtoms: bool = False
    integrator: Integrators = Integrators.langevin


@dataclasses.dataclass(kw_only=True)
class RunSimulationsResponse:
    pdbContent: str | None