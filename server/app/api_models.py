from typing import List, Optional
from pydantic import BaseModel

class Message(BaseModel):
    content: str
    role: str

class Choice(BaseModel):
    finish_reason: str
    index: int
    message: Message

class Usage(BaseModel):
    completion_tokens: int
    prompt_tokens: int
    total_tokens: int

class ChatCompletion(BaseModel):
    choices: List[Choice]
    created: int
    id: str
    model: str
    object: str
    usage: Optional[Usage]

class TutorQuery(BaseModel):
    input: str
    context_uuid: str