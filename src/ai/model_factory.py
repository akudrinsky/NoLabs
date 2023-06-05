from typing import Dict, Union

from .exceptions.unknown_model_ex import UnknownModelException
from .model import ClassificationModel, Folding, BaseModel


def create_model(model_metadata: Dict[str, str]) -> Union[BaseModel, None]:
    assert 'name' in model_metadata
    assert 'type' in model_metadata
    assert 'gpu' in model_metadata

    model_name = model_metadata.get('name')
    model_type = model_metadata.get('type')
    use_gpu = model_metadata.get('gpu')

    if model_type == "classification":
        model_labels = model_metadata.get('labels', [])

        model = ClassificationModel(model_name=model_name, gpu=use_gpu)
        model.load_model()
        model.set_labels(model_labels)

        return model

    if model_type == "folding":
        model = Folding(model_name=model_name, gpu=use_gpu)
        model.load_model()
        
        return model

    raise UnknownModelException()
