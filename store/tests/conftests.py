from rest_framework.test import APIClient
import pytest
from django.contrib.auth.models import User


@pytest.fixture
def api_client():
    return APIClient()


