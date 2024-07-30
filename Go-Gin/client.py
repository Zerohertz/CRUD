import json

import requests
import zerohertzLib as zz

BASE_URL = "http://localhost:8080/users"
LOGGER = zz.logging.Logger("CLIENT")


def create_user():
    url = BASE_URL
    payload = {
        "username": "john_doe",
        "email": "john.doe@example.com",
        "password": "securepassword123",
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    LOGGER.info(f"Create User Response: {response.status_code}\n\t{response.json()}")


def get_all_users():
    url = BASE_URL
    response = requests.get(url)
    users = response.json()
    LOGGER.info(f"Get All Users Response: {response.status_code}\n\t{users}")
    if users:
        return users[0]["id"]
    return None


def get_user_by_id(user_id):
    url = f"{BASE_URL}/{user_id}"
    response = requests.get(url)
    LOGGER.info(
        f"Get User by ID {user_id} Response: {response.status_code}\n\t{response.json()}"
    )


def update_user(user_id):
    url = f"{BASE_URL}/{user_id}"
    payload = {"username": "john_doe_updated", "email": "john.doe.updated@example.com"}
    headers = {"Content-Type": "application/json"}
    response = requests.put(url, data=json.dumps(payload), headers=headers)
    LOGGER.info(
        f"Update User {user_id} Response: {response.status_code}\n\t{response.json()}"
    )


def partial_update_user(user_id):
    url = f"{BASE_URL}/{user_id}"
    payload = {"email": "john.newemail@example.com"}
    headers = {"Content-Type": "application/json"}
    response = requests.patch(url, data=json.dumps(payload), headers=headers)
    LOGGER.info(
        f"Partial Update User {user_id} Response: {response.status_code}\n\t{response.json()}"
    )


def delete_user(user_id):
    url = f"{BASE_URL}/{user_id}"
    response = requests.delete(url)
    LOGGER.info(f"Delete User {user_id} Response: {response.status_code}")


if __name__ == "__main__":
    create_user()
    id = get_all_users()
    get_user_by_id(id)
    update_user(id)
    partial_update_user(id)
    delete_user(id)
    get_all_users()
