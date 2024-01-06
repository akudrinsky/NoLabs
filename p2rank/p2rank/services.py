from p2rank.model import PocketPredictor
from p2rank.api_models import RunP2RankPredictionResponse, RunP2RankPredictionRequest
from p2rank.loggers import Log

__all__ = ['run_p2rank']

def run_p2rank(parameters: RunP2RankPredictionRequest) -> RunP2RankPredictionResponse:
    try:
        model = PocketPredictor()
        pocket_ids = model.predict(
            protein_pdb_file=parameters.protein_file
        )
        return RunP2RankPredictionResponse(pocket_ids=pocket_ids)
    except Exception as e:
        Log.exception()
        return RunP2RankPredictionResponse(pocket_ids=None, errors=['Unable to run p2rank. Internal error', str(e)])
