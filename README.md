### Goal

Create a REST API in Python using FastAPI that allows you to create contacts in HubSpot and synchronize them with ClickUp, while also creating records in an external PostgreSQL database to register each call made to the API.

- [x] Endpoint to create contact on HubSpot

```json
{
  "email": "test@orbidi.com",
  "firstname": "Test",
  "lastname": "Orbidi",
  "phone": "(322) 123-4567",
  "website": "orbidi.com"
}
```

- [] Endpoint to sync HubSpot contacts with ClickUp
- [] use sqlalchemy to connect to a PostgreSQL database
