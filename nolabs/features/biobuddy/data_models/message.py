from typing import Any, List, Union
from pydantic.dataclasses import dataclass


@dataclass
class File:
    name: str
    content: str


@dataclass
class RegularMessage:
    content: str


@dataclass
class FunctionParam:
    name: str
    value: Any = None


@dataclass
class FunctionCall:
    function_name: str
    parameters: List[FunctionParam]


@dataclass
class Message:
    role: str
    message: Union[RegularMessage,FunctionCall]
    type: str