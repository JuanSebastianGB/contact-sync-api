import os
from fastapi import FastAPI, BackgroundTasks
from datetime import datetime

import uvicorn
from hubspotClient import HubSpotClient
from clickup import ClickUpClient
from database import save_api_call
from schemas.schemas import ContactCreateSchema
from utils import validate_contact_data, log_event
from dotenv import load_dotenv

load_dotenv()


app = FastAPI()


@app.get("/get-contacts")
async def get_contacts():
    """
    Retrieves contacts from HubSpot.

    Returns:
        list: A list of contacts retrieved from HubSpot.
    """
    hubspot_client = HubSpotClient(
        access_token=os.environ.get("HUBSPOT_ACCESS_TOKEN"))
    hubspot_contacts = hubspot_client.get_contacts()

    return hubspot_contacts


@app.post("/create-contact", status_code=201)
async def create_contact(contact: ContactCreateSchema):
    """
    Create a new contact.

    This endpoint allows you to create a new contact on HubSpot.

    Parameters:
    - contact: ContactCreateSchema object containing the contact details.

    Returns:
    - If the contact is created successfully on HubSpot, returns a JSON response with the message:
      {"message": "Contact {hubspot_contact_id} created successfully on HubSpot"}.
    - If there is an error creating the contact on HubSpot, returns a JSON response with the error:
      {"error": "Error creating contact on HubSpot"}.

    Note:
    - The access token for HubSpot should be provided as an environment variable named "HUBSPOT_ACCESS_TOKEN".
    - The contact details are validated before creating the contact. If the data is invalid,
      a response with an error message will be returned.

    """

    # create contact on HubSpot
    hubspot_client = HubSpotClient(
        access_token=os.environ.get("HUBSPOT_ACCESS_TOKEN"))
    hubspot_contact_id = hubspot_client.create_contact(contact)

    if (not hubspot_contact_id):
        return {"error": "Error creating contact on HubSpot"}

    result = "success" if hubspot_contact_id else "error"

    # Save API call to database
    save_api_call("/create-contact",
                  contact, result)

    return {"message": f"Contact {hubspot_contact_id} created successfully on HubSpot"}


@app.post("/sync-contacts")
async def sync_contacts(background_tasks: BackgroundTasks):
    """
    Endpoint to initiate the synchronization of contacts from HubSpot to ClickUp.
    """
    # Get contacts from HubSpot
    hubspot_client = HubSpotClient(
        access_token=os.environ.get("HUBSPOT_ACCESS_TOKEN"))
    hubspot_contacts = hubspot_client.get_contacts()

    # Sync contacts with ClickUp in the background
    background_tasks.add_task(sync_contacts_clickup, hubspot_contacts)

    # Save API call to database
    save_api_call("/sync-contacts", None, None)

    return {"message": "Sync started successfully"}


def sync_contacts_clickup(contacts):
    """
    Synchronizes contacts with ClickUp tasks.

    Parameters:
    - contacts (list): A list of contact dictionaries.

    Each contact dictionary should have the following structure:
    {
        "email": str,             # Email address of the contact.
        "estado_clickup": bool    # Indicates if the contact is already synced with ClickUp.
    }

    The function iterates over the contacts list and checks if each contact is already synced with ClickUp.
    If a contact is not synced, it creates a ClickUp task for that contact and updates its estado_clickup value to True.

    After processing all contacts, it logs an event indicating that the synchronization is finished.
    """
    clickup_client = ClickUpClient(
        token=os.environ.get("CLICKUP_ACCESS_TOKEN"), list_id=os.environ.get("CLICKUP_LIST_ID"))
    for contact in contacts:
        if not contact.get('estado_clickup'):
            clickup_client.create_task(contact)
            contact['estado_clickup'] = True

    log_event("Sync finished")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
