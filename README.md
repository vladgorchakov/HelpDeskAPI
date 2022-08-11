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
    2)  GET access and refresh tokens:
        - URL: http://0.0.0.0:8000/api/v1/token/
        - HTTP METHOD: [POST]
        - example:
            {
                "username": "name",
                "password": "12345nameuserpassword"
            }

    3) GET new access token:
        - URL: http://0.0.0.0:8000/api/v1/token/
        - HTTP METHOD: [POST]
        - example:
            {
                "refresh": "{YOUR_REFRESH_TOKENS}"
            }


    4)  GET list of tickets
        - URL: http://0.0.0.0:8000/api/v1/tickets/
        - HTTP METHOD [GET]
        - Authorization HEADER: Bearer {YOUR_ACCESS_TOKEN}

    5) CREATE ticket
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

    6) READ ticket
        - URL: http://0.0.0.0:8000/api/v1/tickets/{id}/
        - HTTP METHOD: [GET]
        - Authorization HEADER: Bearer {YOUR_ACCESS_TOKEN}
    
    7) UPDATE ticket
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
            
    8) DELETE ticket
        - URL: http://0.0.0.0:8000/api/v1/tickets/{id}/
        - HTTP METHOD: [DELETE]
        - Authorization HEADER: Bearer {YOUR_ACCESS_TOKEN}

    9) GET list of messages
        - URL: http://0.0.0.0:8000/api/v1/messaage/
        - HTTP METHOD: [GET]
        - Authorization HEADER: Bearer {YOUR_ACCESS_TOKEN}
    
    10) CREATE message
        - URL: http://0.0.0.0:8000/api/v1/messaage/
        - HTTP METHOD: [POST]
        - Authorization HEADER: Bearer {YOUR_ACCESS_TOKEN}
        - EXAMPLE:
            {
                "ticket": "5",
                "text": "new message for ticket id=5"
            }
    
    11) UPDATE message
        - URL: http://0.0.0.0:8000/api/v1/messaage/
        - HTTP METHOD: [PUT]
        - Authorization HEADER: Bearer {YOUR_ACCESS_TOKEN}
        - EXAMPLE:
            {
                "text": "Update message for ticket id=5"
            }
    
    12) DELETE message
        - URL: http://0.0.0.0:8000/api/v1/messaage/
        - HTTP METHOD: [DELETE]
        - Authorization HEADER: Bearer {YOUR_ACCESS_TOKEN}
