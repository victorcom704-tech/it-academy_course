import pytest


# 1.1
@pytest.fixture
def book_data():
    return {"title": "1984", "author": "George Orwell", "pages": 328}


# 1.2
@pytest.fixture
def temp_list():
    templ = [1, 2, 3]
    yield templ
    templ.clear()


# 1.4
@pytest.fixture
def base_url():
    return "https://example.com"


@pytest.fixture
def users_endpoint(base_url):
    return f"{base_url}/users"
