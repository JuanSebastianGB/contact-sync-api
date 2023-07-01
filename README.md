# Contact Sync API

This project implements a Contact Sync API using FastAPI in Python. The API allows you to create contacts in HubSpot, synchronize them with ClickUp, and record API calls in a PostgreSQL database. It provides the following endpoints:

## Endpoints

### Retrieve Contacts from HubSpot

- **Endpoint**: `/get-contacts`
- **Method**: GET
- **Description**: Retrieves contacts from HubSpot.
- **Returns**: A list of contacts retrieved from HubSpot.

### Create Contact in HubSpot

- **Endpoint**: `/create-contact`
- **Method**: POST
- **Description**: Creates a new contact in HubSpot.
- **Parameters**:
  - `contact`: ContactCreateSchema object containing the contact details.
- **Returns**:
  - If the contact is created successfully on HubSpot, returns a JSON response with the message: `{"message": "Contact {hubspot_contact_id} created successfully on HubSpot"}`.
  - If there is an error creating the contact on HubSpot, returns a JSON response with the error: `{"error": "Error creating contact on HubSpot"}`.

### Synchronize Contacts between HubSpot and ClickUp

- **Endpoint**: `/sync-contacts`
- **Method**: POST
- **Description**: Initiates the synchronization of contacts from HubSpot to ClickUp.
- **Returns**: A JSON response with the message: `{"message": "Sync started successfully"}`.

## Setup and Configuration

To run the Contact Sync API, follow these steps:

1.  Clone the repository: `git clone https://github.com/JuanSebastianGB/contact-sync-api.git`
2.  Install the dependencies: `pip install -r requirements.txt`
3.  Set up the following environment variables in a `.env` file:
    - `HUBSPOT_ACCESS_TOKEN`: Access token for HubSpot.
    - `CLICKUP_ACCESS_TOKEN`: Access token for ClickUp.
    - `CLICKUP_LIST_ID`: ID of the ClickUp list.
4.  Start the server: `python main.py`
5.  The API will be accessible at `http://localhost:8000`.

## Additional Features

The Contact Sync API includes the following additional features:

- Logging: Events are logged to record important information.
- Database: API calls are saved to a PostgreSQL database hosted on an external server. The database connection details are provided in the environment variables.

## Resources

- [HubSpot Contacts API](https://developers.hubspot.com/docs/api/crm/contacts): API documentation for HubSpot Contacts.
- [ClickUp API](https://clickup.com/api/): API documentation for ClickUp.
- PostgreSQL Database:
  - Host: `db.g97.io`
  - Port: `5432`
  - User: `developer`
  - Password: `qS*7Pjs3v0kw`
  - Database Name: `data_analyst`

## Repository

The code for this project is hosted in the following GitHub repository: [Link to GitHub Repository](https://github.com/JuanSebastianGB/contact-sync-api)
