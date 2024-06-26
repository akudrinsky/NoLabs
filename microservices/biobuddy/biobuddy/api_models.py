from __future__ import annotations

from langchain_core.messages import BaseMessage
from pydantic import dataclasses as pcdataclass
from typing import List, Optional, Dict, Any

from openai.types.chat import ChatCompletionMessage

from biobuddy.mixins import BaseModelMixin


@pcdataclass.dataclass
class SendMessageToBioBuddyRequest(BaseModelMixin):
    message_content: str
    # TODO: send only the last N tokens based on model's context window
    previous_messages: List[Dict[str, str]]
    tools: List[Dict[str, Any]]
    job_id: Optional[str] = None


@pcdataclass.dataclass
class SendMessageToBioBuddyResponse(BaseModelMixin):
    reply_type: str
    content: str

@pcdataclass.dataclass
class IsJobRunningResponse:
    is_running: bool
