TICKET_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "create_time": {"type": "string"},
        "update_time": {"type": "string"},
        "title": {"type": "string"},
        "description": {"type": "string"},
        "status": {"type": "number"},
        "user": {"type": "number"}
    },
    "required": ["id"]
}
