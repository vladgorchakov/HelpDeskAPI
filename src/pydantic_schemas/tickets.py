from pydantic import BaseModel, validator, ValidationError


class Ticket(BaseModel):
    id: str
    title: str
    description: str
    user: str
    status: int
    create_time: str
    update_time: str

