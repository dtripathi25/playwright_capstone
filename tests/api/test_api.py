from utils.api_models import UserResponse
from utils.json_utils import compare_json
def test_get_users(api_request_context):
    response = api_request_context.get(
        "https://jsonplaceholder.typicode.com/users"
    )

    assert response.status == 200
    
    
def test_get_users_response_body(api_request_context):
    response = api_request_context.get(
        "https://jsonplaceholder.typicode.com/users"
    )

    assert response.status == 200

    users = response.json()

    assert len(users) > 0

    user = UserResponse(users[0])

    assert user.name
    assert user.email
    
    
def test_create_user(api_request_context):
    response = api_request_context.post(
        "https://jsonplaceholder.typicode.com/users",
        data={
            "name": "Devesh",
            "username": "devesh123",
            "email": "devesh@example.com"
        }
    )

    assert response.status == 201

    user = response.json()

    assert user["name"] == "Devesh"
    assert user["username"] == "devesh123"   
    
    
def test_update_user(api_request_context):
    response = api_request_context.put(
        "https://jsonplaceholder.typicode.com/users/1",
        data={
            "name": "Devesh Updated",
            "username": "devesh_updated"
        }
    )

    assert response.status == 200

    user = response.json()

    assert user["name"] == "Devesh Updated"
    assert user["username"] == "devesh_updated"
    
def test_delete_user(api_request_context):
    response = api_request_context.delete(
        "https://jsonplaceholder.typicode.com/users/1"
    )

    assert response.status == 200
    
    
def test_find_user_by_name(api_request_context):
    response = api_request_context.get(
        "https://jsonplaceholder.typicode.com/users"
    )

    assert response.status == 200

    users = response.json()

    user = next(
        (u for u in users if u["name"] == "Leanne Graham"),
        None
    )

    assert user is not None
    assert user["email"] == "Sincere@april.biz"
    
    
def test_deep_json_comparison():
    actual = {
        "user": {
            "name": "Leanne Graham",
            "address": {
                "city": "Gwenborough"
            }
        }
    }

    expected = {
        "user": {
            "name": "Leanne Graham",
            "address": {
                "city": "Gwenborough"
            }
        }
    }

    assert actual == expected
    assert compare_json(actual, expected) is None