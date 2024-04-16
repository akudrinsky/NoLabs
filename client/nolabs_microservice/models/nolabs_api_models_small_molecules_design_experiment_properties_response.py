# coding: utf-8

"""
    NoLabs

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel
from nolabs_microservice.models.pdb_file import PdbFile
from nolabs_microservice.models.pdb_file_name import PdbFileName
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class NolabsApiModelsSmallMoleculesDesignExperimentPropertiesResponse(BaseModel):
    """
    NolabsApiModelsSmallMoleculesDesignExperimentPropertiesResponse
    """ # noqa: E501
    center_x: Optional[Any]
    center_y: Optional[Any]
    center_z: Optional[Any]
    size_x: Optional[Any]
    size_y: Optional[Any]
    size_z: Optional[Any]
    batch_size: Optional[Any]
    minscore: Optional[Any]
    epochs: Optional[Any]
    pdb_file: PdbFile
    pdb_file_name: PdbFileName
    __properties: ClassVar[List[str]] = ["center_x", "center_y", "center_z", "size_x", "size_y", "size_z", "batch_size", "minscore", "epochs", "pdb_file", "pdb_file_name"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of NolabsApiModelsSmallMoleculesDesignExperimentPropertiesResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of pdb_file
        if self.pdb_file:
            _dict['pdb_file'] = self.pdb_file.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pdb_file_name
        if self.pdb_file_name:
            _dict['pdb_file_name'] = self.pdb_file_name.to_dict()
        # set to None if center_x (nullable) is None
        # and model_fields_set contains the field
        if self.center_x is None and "center_x" in self.model_fields_set:
            _dict['center_x'] = None

        # set to None if center_y (nullable) is None
        # and model_fields_set contains the field
        if self.center_y is None and "center_y" in self.model_fields_set:
            _dict['center_y'] = None

        # set to None if center_z (nullable) is None
        # and model_fields_set contains the field
        if self.center_z is None and "center_z" in self.model_fields_set:
            _dict['center_z'] = None

        # set to None if size_x (nullable) is None
        # and model_fields_set contains the field
        if self.size_x is None and "size_x" in self.model_fields_set:
            _dict['size_x'] = None

        # set to None if size_y (nullable) is None
        # and model_fields_set contains the field
        if self.size_y is None and "size_y" in self.model_fields_set:
            _dict['size_y'] = None

        # set to None if size_z (nullable) is None
        # and model_fields_set contains the field
        if self.size_z is None and "size_z" in self.model_fields_set:
            _dict['size_z'] = None

        # set to None if batch_size (nullable) is None
        # and model_fields_set contains the field
        if self.batch_size is None and "batch_size" in self.model_fields_set:
            _dict['batch_size'] = None

        # set to None if minscore (nullable) is None
        # and model_fields_set contains the field
        if self.minscore is None and "minscore" in self.model_fields_set:
            _dict['minscore'] = None

        # set to None if epochs (nullable) is None
        # and model_fields_set contains the field
        if self.epochs is None and "epochs" in self.model_fields_set:
            _dict['epochs'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of NolabsApiModelsSmallMoleculesDesignExperimentPropertiesResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "center_x": obj.get("center_x"),
            "center_y": obj.get("center_y"),
            "center_z": obj.get("center_z"),
            "size_x": obj.get("size_x"),
            "size_y": obj.get("size_y"),
            "size_z": obj.get("size_z"),
            "batch_size": obj.get("batch_size"),
            "minscore": obj.get("minscore"),
            "epochs": obj.get("epochs"),
            "pdb_file": PdbFile.from_dict(obj.get("pdb_file")) if obj.get("pdb_file") is not None else None,
            "pdb_file_name": PdbFileName.from_dict(obj.get("pdb_file_name")) if obj.get("pdb_file_name") is not None else None
        })
        return _obj


