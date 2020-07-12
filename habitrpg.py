from enum import Enum
from src.tags import Tags


class TaskTypes(Enum):
    HABIT = "habit"
    DAILY = "daily"
    TODO = "todo"


class HabitRPG:
    task_types = [task_enum.value for task_enum in TaskTypes]

    def __init__(self, user, password):
        self.Tags = Tags(user, password)

    def _validate_task_data(self, data, task_type):
        task_name = data.get("name")
        if not task_name:
            return {}

        # extra validations go here

    # def create_user_habit(self, data):
    #     CREATE_URL = f"{self.base_url}/tasks/user"

    #     self._validate_task_data(data, "habit")

    #     payload = {
    #         "text": data.get("name"),
    #         "type": "habit",
    #         "tags": data.get("tags", []),
    #         "alias": data.get("alias", "per"),
    #         "priority": data.get("priority", "1"),
    #         "up": data.get("up", True),
    #         "down": data.get("down", True),
    #     }
    #     response = self.post_request(CREATE_URL, payload)
    #     return response.get("data")

    # def create_user_daily(self, data):
    #     CREATE_URL = f"{self.base_url}/tasks/user"
    #     task_name = data.get("name")
    #     if not task_name:
    #         return {}

    #     payload = {
    #         "text": task_name,
    #         "type": "daily",
    #         "tags": data.get("tags", []),
    #         "attribute": data.get("alias", "per"),
    #         "priority": data.get("priority", "1"),
    #         "frequency": data.get("frequency", "daily"),
    #     }
    #     response = self.post_request(CREATE_URL, payload)
    #     return response.get("data")

    # def create_user_todo(self, data):
    #     CREATE_URL = f"{self.base_url}/tasks/user"
    #     task_name = data.get("name")
    #     if not task_name:
    #         return {}

    #     payload = {
    #         "text": task_name,
    #         "type": "todo",
    #         "tags": data.get("tags", []),
    #         "attribute": data.get("attribute", "per"),
    #         "priority": data.get("priority", "1"),
    #     }
    #     response = self.post_request(CREATE_URL, payload)
    #     return response.get("data")

    # def get_tags(self):
    #     GET_URL = f"{self.base_url}/tags"
    #     response = self.get_request(GET_URL)
    #     return response.get("data")
