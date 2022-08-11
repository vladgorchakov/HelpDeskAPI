# helpdeskAPI

## Endpoints of helpdesk API:
    1)  REGISTER a new user:
        - URL: http://0.0.0.0:8000/api/v1/auth/users/
        - HTTP METHOD: [POST]
        - example:
            {
                "email": "name@host.com",
                "username": "name",
                "password": "12345nameuserpassword"
            }
    2)  GET tokens:
        - URL: http://0.0.0.0:8000/api/v1/token/
        - HTTP METHOD: [POST]
        - example:
            {
                "username": "name",
                "password": "12345nameuserpassword"
            }

    3)  GET list of tickets
        - URL: http://0.0.0.0:8000/api/v1/tickets/
        - HTTP METHOD [GET]
        - Authorization HEADER: Bearer {YOUR_ACCESS_TOKEN}

    4) CREATE ticket
        - URL: http://0.0.0.0:8000/api/v1/tickets/
        - HTTP METHOD [POST]
        - Authorization HEADER: Bearer {YOUR_ACCESS_TOKEN}
        - examples:
                ONE MESSAGE:
            {
                "title": "Title of my ticket",
                "description": "Description of my ticket",
                "messages": [
                    {
                        "text": "Text of message for my ticket"
                    }
                ]
            }
                
                MANY MESSAGES:
            {
                "title": "Title of my ticket",
                "description": "Description of my ticket",
                "messages": [    
                    {
                        "text": "Text 1 of message for my ticket"
                    },
                    {
                        "text": "Text 2 of message for my ticket"
                    },
                    {
                        "text": "Text 3 of message for my ticket"
                    }
                ]
            }
                WITHOUT MESSAGES:
            {
                "title": "Title of my ticket",
                "description": "Description of my ticket",
                "messages": []
            }

    5) READ ticket
        - URL: http://0.0.0.0:8000/api/v1/tickets/{id}/
        - HTTP METHOD: [GET]
        - Authorization HEADER: Bearer {YOUR_ACCESS_TOKEN}
    
    6) UPDATE ticket
        - URL: http://0.0.0.0:8000/api/v1/tickets/{id}/
        - HTTP METHOD: [PUT]
        - Authorization HEADER: Bearer {YOUR_ACCESS_TOKEN}
        - Example:
            USER:
            {
                "title": "New title of my ticket",
                "description": "New description of my ticket"
            }
            
            SUPPORT (STAFF)
            {
                "status": "1"
            }
            
    7) DELETE ticket
        - URL: http://0.0.0.0:8000/api/v1/tickets/{id}/
        - HTTP METHOD: [DELETE]
        - Authorization HEADER: Bearer {YOUR_ACCESS_TOKEN}

    8) GET list of messages
        - URL: http://0.0.0.0:8000/api/v1/messaage/
        - HTTP METHOD: [GET]
        - Authorization HEADER: Bearer {YOUR_ACCESS_TOKEN}
    
    9) CREATE message
        - URL: http://0.0.0.0:8000/api/v1/messaage/
        - HTTP METHOD: [POST]
        - Authorization HEADER: Bearer {YOUR_ACCESS_TOKEN}
        - EXAMPLE:
            {
                "ticket": "5",
                "text": "new message for ticket id=5"
            }
    
    10) UPDATE message
        - URL: http://0.0.0.0:8000/api/v1/messaage/
        - HTTP METHOD: [PUT]
        - Authorization HEADER: Bearer {YOUR_ACCESS_TOKEN}
        - EXAMPLE:
            {
                "text": "Update message for ticket id=5"
            }
    
    10) DELETE message
        - URL: http://0.0.0.0:8000/api/v1/messaage/
        - HTTP METHOD: [DELETE]
        - Authorization HEADER: Bearer {YOUR_ACCESS_TOKEN}
