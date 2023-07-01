
from calendar import c
import requests


class HubSpotClient:

    def __init__(self, access_token):
        self.access_token = access_token

    def create_contact(self, contact):
        """
        Creates a contact in the HubSpot CRM.

        Parameters:
            contact (object): The contact object containing contact details.

        Returns:
            str: The ID of the created contact if successful, otherwise None.
        """
        endpoint = "https://api.hubspot.com/crm/v3/objects/contacts"
        headers = {"Authorization": f"Bearer {self.access_token}",
                   "Content-Type": "application/json"}
        data = {
            "properties": {
                "email": contact.email,
                "firstname": contact.firstname,
                "lastname": contact.lastname,
                "phone": contact.phone,
                "website": contact.website,
            }
        }
        response = requests.post(endpoint, headers=headers, json=data)
        if response.status_code == 201:
            return response.json()["id"]
        return None

    def get_contacts(self):
        """
        Retrieves a list of contacts from the HubSpot CRM.

        Returns:
            A list of contact objects retrieved from the HubSpot CRM.

        Raises:
            - Any exceptions raised by the requests library.
        """
        endpoint = "https://api.hubspot.com/crm/v3/objects/contacts"
        headers = {"Authorization": f"Bearer {self.access_token}"}
        response = requests.get(endpoint, headers=headers)
        if response.status_code == 200:
            return response.json()["results"]
        return []
