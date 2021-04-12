import json
import pytest

pytestmark = [pytest.mark.django_db]


@pytest.mark.parametrize(
    "data, status_code, response_body",
    [
        (
            None,
            400,
            {
                "full_name": ["This field is required."],
                "email": ["This field is required."],
                "password": ["This field is required."],
            },
        ),
        (
            dict(full_name="", email="", password=""),
            400,
            {
                "full_name": ["This field may not be blank."],
                "email": ["This field may not be blank."],
                "password": ["This field may not be blank."],
            },
        ),
    ],
)
def test_empty_message_error(api, data, status_code, response_body):
    response = api.post("/api/user/registration/", data, format="json")

    assert json.loads(response.content.decode("utf-8")) == response_body
    assert response.status_code == status_code


def test_unique_user(api, create_user):
    user = create_user(full_name="Alesha", email="alesha@a.com")
    data = dict(full_name="Alesha", email="alesha@a.com", password="alesha1234")

    response = api.post("/api/user/registration/", data, format="json")
    response_dict = json.loads(response.content.decode("utf-8"))

    assert response.status_code == 400
    assert response_dict["email"][0] == "This email already exists"
    assert response_dict["full_name"][0] == "This full name already exists"


def test_good_registration(api):
    data = dict(full_name="Wata", email="Wata@a.com", password="Wata12345")
    response = api.post("/api/user/registration/", data, format="json")

    assert response.status_code == 201
