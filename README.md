# helpdeskAPI

## Endpoints of helpdesk API:
    1)  Register a new user:
        - URL: http://0.0.0.0:8000/api/v1/auth/users/
        - HTTP METHOD: [POST]
        - example:
            {
                "email": "name@host.com",
                "username": "name",
                "password": "12345nameuserpassword"
            }
    2)  Get tokens:
        - URL: http://0.0.0.0:8000/api/v1/token/
        - HTTP METHOD: [POST]
        - example:
            {
                "username": "name",
                "password": "12345nameuserpassword"
            }
    3)  Get list of tickets
        - URL: http://0.0.0.0:8000/api/v1/tickets/
        - HTTP METHOD [GET]
        - Authorization HEADER: Bearer {YOUR_ACCESS_TOKEN}
    4) Create ticket
        - URL: http://0.0.0.0:8000/api/v1/tickets/
        - HTTP METHOD [GET]
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
