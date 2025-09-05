import requests
from requests import Response

import data
import sender_stand_request


def get_kit_body(kit_name):
    current_body = data.kit_body.copy()
    current_body["name"] = kit_name
    return current_body

def positive_assert(kit_body):
    response = sender_stand_request.post_new_user(data.user_body)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body):
    response = sender_stand_request.post_new_user(data.user_body)
    assert response.status_code == 400

def test_create_kit_name():
