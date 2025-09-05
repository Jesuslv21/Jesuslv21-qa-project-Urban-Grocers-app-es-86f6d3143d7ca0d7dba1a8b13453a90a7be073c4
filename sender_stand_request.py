import configuration
import requests
import data


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

def post_new_client_kit(kit_body, auth_token):
    new_headers = data.headers.copy()
    new_headers["Authorization"] = "Bearer " + auth_token

    new_headers = {
        "Content-Type": "application/json"
        "authorization": "Bearer "
    }
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=kit_body,
                         headers=new_headers)




