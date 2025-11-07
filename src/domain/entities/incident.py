from datetime import datetime

from pydantic.dataclasses import dataclass


@dataclass
class IncidentEntity:
    id: int
    text: str
    description: str
    status: str
    source: str
    created_at: datetime


@dataclass
class CreateIncidentRequestEntity:
    text: str
    description: str
    status: str
    source: str


@dataclass
class UpdateIncidentRequestEntity:
    status: str
