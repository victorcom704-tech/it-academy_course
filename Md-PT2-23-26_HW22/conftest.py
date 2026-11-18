import pytest
import os
from practice_calculator import Calculator


# 1.3
@pytest.fixture
def env_setup():
    os.environ["APP_MODE"] = "testing"
    yield
    del os.environ["APP_MODE"]


# 1.5
@pytest.fixture(params=(2, 4, 6, 8))
def number(request):
    return request.param


# 1.7
@pytest.fixture
def calculator():
    return Calculator()
