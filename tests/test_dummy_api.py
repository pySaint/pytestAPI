from uuid import uuid4
import requests
from requests import Response


def test_can_user_create_task(create_task_api, get_task_api):
    user_id = f"user_{uuid4().hex}"
    random_task_content = f"task content: {uuid4().hex}"
    payload = {
        "user_id": user_id,
        "content": random_task_content,
    }

    create_task_response = create_task_api(payload=payload)
    print(create_task_response.json())
    assert create_task_response.status_code == 200

    task_id = create_task_response.json()["task"]["task_id"]
    get_task_response = get_task_api(task_id=task_id)

    assert get_task_response.status_code == 200
    print(get_task_response)
    assert get_task_response.json()["content"] == random_task_content


def test_can_user_list_tasks(create_task_api, get_task_list_for_user_api):
    # Create a new user for this test.
    user_id = f"user_{uuid4().hex}"

    # Create 3 tasks for this user.
    for i in range(3):
        payload = {
            "user_id": user_id,
            "task_id": f"task_{i}",
        }
        create_task_api(payload=payload)

    # List the tasks for this user.
    task_list_response = get_task_list_for_user_api(user_id=user_id)
    print(task_list_response.json())
    tasks = task_list_response.json()["tasks"]
    assert len(tasks) == 3


def test_can_user_update_task(create_task_api, update_task_api, get_task_api):
    # Create a new user for this test.
    user_id = f"user_{uuid4().hex}"
    payload = {
        "user_id": user_id,
        "content": "task content",
    }

    create_response = create_task_api(payload=payload)
    task_id = create_response.json()["task"]["task_id"]

    # Update the task with new content.
    new_task_content = f"updated task content: {uuid4().hex}"
    payload = {
        "content": new_task_content,
        "task_id": task_id,
        "is_done": True,
    }
    update_task_response = update_task_api(payload=payload)
    assert update_task_response.status_code == 200

    get_task_response = get_task_api(task_id=task_id)
    assert get_task_response.status_code == 200
    assert get_task_response.json()["content"] == new_task_content
    assert get_task_response.json()["is_done"] is True


def test_can_user_delete_task(create_task_api, delete_task_api, get_task_api):
    user_id = f"user_{uuid4().hex}"
    payload = {
        "user_id": user_id,
        "content": "task1",
    }
    create_response = create_task_api(payload=payload)
    task_id = create_response.json()["task"]["task_id"]
    print(create_response.json())

    # Delete the task.
    delete_task_api(task_id=task_id)

    # We shouldn't be able to get the task anymore.
    get_task_response = get_task_api(task_id=task_id)
    assert get_task_response.status_code == 404
