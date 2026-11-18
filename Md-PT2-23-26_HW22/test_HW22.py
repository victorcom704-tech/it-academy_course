import pytest
from HW22 import book_data, temp_list, base_url, users_endpoint
import os
from app import process_files, read_config, generate_password


# 1.1
def test_book_pages(book_data):
    assert book_data["pages"] > 300


# 1.2
def test_temp_list(temp_list):
    temp_list.append(4)
    assert len(temp_list) == 4


# 1.3
@pytest.mark.usefixtures("env_setup")
def test_app_mode():
    assert os.environ.get("APP_MODE") == "testing"


# 1.4
def test_users_endpoint(users_endpoint):
    assert users_endpoint == "https://example.com/users"


# 1.5
def test_is_even(number):
    assert number % 2 == 0


# 1.6
def test_tmp_path(tmp_path):
    file_path = tmp_path / "hello.txt"
    file_path.write_text("Pytest is awesome")

    assert file_path.exists()
    assert file_path.read_text() == "Pytest is awesome"


# 2.1
def test_process_files(mocker):
    mock_sleep = mocker.patch("app.time.sleep")
    res = process_files()
    mock_sleep.assert_called_once_with(3)
    assert res == "processed"


# 2.2
def test_read_config(mocker):
    mock_file = mocker.mock_open(read_data="host=localhost\n")
    mocker.patch("app.open", mock_file)
    res = read_config("config.txt")
    assert res == "host=localhost"
    mock_file.assert_called_once_with("config.txt", "r")


# 2.3
def test_generate_password(mocker):
    mock_choice = mocker.patch(
        "app.random.choice",
        side_effect=("a", "a", "a", "a", "b", "b", "b", "b"),
    )
    res = generate_password()
    assert res == "aaaabbbb"
    assert mock_choice.call_count == 8
