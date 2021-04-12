import pytest


def test_auth(api, get_or_create_token):
    token = get_or_create_token
    api.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    response = api.get("/api/user/")

    assert response.status_code == 200
    assert response.data['email'] == "tonino@a.com"
