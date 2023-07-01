import requests


class ClickUpClient:
    def __init__(self, token, list_id):
        self.token = token
        self.list_id = list_id

    def create_task(self, contact):
        """
        Creates a task in ClickUp for the given contact.

        Args:
            contact (dict): The contact information.

        Returns:
            None
        """
        endpoint = f"https://api.clickup.com/api/v2/list/{self.list_id}/task"
        headers = {"Authorization": self.token,
                   "Content-Type": "application/json"}
        data = {"name": f"Contact: {contact['id']}"}
        response = requests.post(endpoint, headers=headers, json=data)
        if response.status_code == 200:
            contact['estado_clickup'] = True
