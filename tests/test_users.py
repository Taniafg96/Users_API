from unittest import TestCase
from fastapi.testclient import TestClient
from main import app
from src.models.user_model import UsersModel

class TestUsers(TestCase):
    valid_user = {
        "name": "test_user",
        "email": "hh@dgjkdhjgjf.com",
        "is_active": True,
        "is_superuser": False,
        "created_at": "2023-10-15T23:48:36",
        "updated_at": "2023-10-22T19:09:58"
        }
    def test_get_all_users(self):
        response = TestClient(app).get("/users/all")
        user = response.json()
        assert UsersModel.model_validate(user[0])
    
    def test_get_one_user_by_id(self):
        id = 1
        response = TestClient(app).get(f"/users/{id}")
        user = response.json()
        assert UsersModel.model_validate(user)