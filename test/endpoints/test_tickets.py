import requests
from src.endpoints import SERVICE_URL
from src.baseclasses.response import Response
from src.pydantic_schemas.tickets import Ticket

headers={'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYxNTk0NzQ2LCJqdGkiOiI2MGQyNjY1NmFlODE0MDkwYmQ5NzZkNWY3Y2FmOTcxNiIsInVzZXJfaWQiOjN9.oRL_WLd5pZ-PmgsVVzlUbdDh3gYF89WhXpKqgI5IZbw'}


def test_getting_tickets(get_token):
    response = Response(requests.get(url=SERVICE_URL, headers=headers))
    response.assert_status_code(200)
    response.validate(Ticket)




