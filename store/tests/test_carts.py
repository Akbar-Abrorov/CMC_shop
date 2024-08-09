import pytest
from rest_framework import status
from model_bakery import baker
from rest_framework.test import APIClient
from store.models import Cart, CartItem, Product

@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
class TestCreateCart:
    def test_create_cart_returns_201(self, api_client):
        response = api_client.post('/store/carts/', {})
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] is not None

@pytest.mark.django_db
class TestDeleteCart:
    def test_if_cart_exists_returns_204(self, api_client):
        cart = baker.make(Cart)
        response = api_client.delete(f'/store/carts/{cart.id}/')
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Cart.objects.count() == 0