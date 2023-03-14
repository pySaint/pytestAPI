
import pytest
import requests


@pytest.fixture
def api_url():
    return "https://todo.pixegami.io/"


@pytest.fixture
def api_headers():
    return {"Content-Type": "application/json"}


@pytest.fixture
def get_task_api(api_url, api_headers):
    def _api_get(task_id):
        response = requests.get(f"{api_url}/get-task/{task_id}", headers=api_headers)
        return response
    return _api_get


@pytest.fixture
def get_task_list_for_user_api(api_url, api_headers):
    def _api_get(user_id):
        response = requests.get(f"{api_url}/list-tasks/{user_id}", headers=api_headers)
        return response
    return _api_get


@pytest.fixture
def create_task_api(api_url, api_headers):
    def _api_put(payload):
        response = requests.put(f"{api_url}/create-task", headers=api_headers, json=payload)
        return response
    return _api_put


@pytest.fixture
def update_task_api(api_url, api_headers):
    def _api_put(payload):
        response = requests.put(f"{api_url}/update-task", headers=api_headers, json=payload)
        return response
    return _api_put


@pytest.fixture
def delete_task_api(api_url, api_headers):
    def _api_delete(task_id):
        response = requests.delete(f"{api_url}delete-task/{task_id}", headers=api_headers)
        return response
    return _api_delete

