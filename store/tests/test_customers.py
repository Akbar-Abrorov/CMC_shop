from model_bakery import baker
import pytest
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.exceptions import ErrorDetail
from rest_framework.test import APIClient
from store.models import Customer

@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
class TestCreateCustomer:
    def test_if_user_is_anonymous_returns_401(self, api_client):
        response = api_client.post('/store/customers/', {'phone': '1234567890', 'birth_date': '1990-01-01', 'membership': 'B'})
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_returns_403(self, api_client):
        api_client.force_authenticate(user={})
        response = api_client.post('/store/customers/', {'phone': '1234567890', 'birth_date': '1990-01-01', 'membership': 'B'})
        assert response.status_code == status.HTTP_403_FORBIDDEN
