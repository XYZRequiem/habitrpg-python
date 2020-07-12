from src.base.base_class import BaseClass


class Tags(BaseClass):
    def __init__(self, user, password):
        super().__init__(user, password)
        self.tag_url = f"{self.base_url}/tags"

    def create(self, tag_name: str) -> dict:
        payload = {"name": tag_name}

        response = self.post_request(self.tag_url, payload)
        return response.get("data")

    def delete(self, tag_id: int) -> dict:
        DELETE_URL = f"{self.tag_url}/{tag_id}"
        response = self.delete_request(DELETE_URL)
        return response.get("data")

    def get_by_id(self, tag_id: int) -> dict:
        GET_URL = f"{self.tag_url}/{tag_id}"
        response = self.get_request(GET_URL)
        return response.get("data")

    def get(self):
        response = self.get_request(self.tag_url)
        return response.get("data")

    def reorder_tags(self, tag_data: dict) -> dict:
        REORDER_URL = f"{self.tag_url}/reorder-tags"
        response = self.post_request(REORDER_URL, tag_data)
        return response.get("data")

    def update(self, tag_id: int, tag_name: str) -> dict:
        UPDATE_URL = f"{self.tag_url}/{tag_id}"
        payload = {"name": tag_name}
        response = self.put_request(UPDATE_URL, payload)
        return response.get("data")
