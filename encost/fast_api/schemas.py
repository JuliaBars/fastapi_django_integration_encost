from datetime import datetime
from typing import Optional

from pydantic import BaseModel, validator

from encost.settings import STATE_START


class Schema(BaseModel):
    input_start: str = STATE_START

    @validator("input_start", pre=True, always=True)
    def parse_input_start(cls, value):
        if isinstance(value, str):
            return str(datetime.fromisoformat(value).timestamp())
        raise ValueError("input_start must be a string")


class ClientFA(BaseModel):
    client_id: int
    client_name: str
    client_info: Optional[str] = None


class ClientInfoFA(BaseModel):
    info_id: int
    info: str


class EndpointFA(BaseModel):
    endpoint_id: int
    endpoint_name: str


class EndpointStatesFA(BaseModel):
    endpoint_states_id: int
    endpoint_id: int
    client_id: int
    state_name: str
    state_reason: str
    state_start: int
    state_end: int | None
    state_id: str
    group_id: str
    reason_group: str
    info: dict
