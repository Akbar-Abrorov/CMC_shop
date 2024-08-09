import pytest
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from store.models import Product, OrderItem


@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
class TestCreateProduct:
    def test_if_user_is_anonymous_returns_401(self, api_client):
        response = api_client.post('/store/products/', {'title': 'a', 'unit_price': 10})
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_returns_403(self, api_client):
        api_client.force_authenticate(user={})
        response = api_client.post('/store/products/', {'title': 'a', 'unit_price': 10})
        assert response.status_code == status.HTTP_403_FORBIDDEN
