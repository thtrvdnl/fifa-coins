import uuid
import pytest

from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token


@pytest.fixture
def test_password():
    return "strong-test-pass"


@pytest.fixture
def create_user(db, django_user_model, test_password):
    def make_user(**kwargs):
        print(kwargs)
        kwargs["password"] = test_password
        if "email" not in kwargs:
            raise ValueError
        return django_user_model.objects.create_user(**kwargs)

    return make_user


@pytest.fixture
def api():
    return APIClient()


@pytest.fixture
def get_or_create_token(db, create_user):
    user = create_user(email="tonino@a.com")
    token, _ = Token.objects.get_or_create(user=user)
    return token
