import pytest
import re

from controllers import LookUpController


class MockResponse:

    def __init__(self, content, status_code):
        self.content = content
        self.status_code = status_code


@pytest.fixture
def mock_file():
    return './list_of_ips.txt'


@pytest.fixture
def mock_request(mocker):
    mocked = mocker.patch('clients.requests.get')
    mocked.return_value = MockResponse('{"_content": {"ip":"216.235.211.155","country_code":"US","country_name":"United States","region_code":"","region_name":"","city":"","zip_code":"","time_zone":"AmericagChicago","latitude":37.751,"longitude":-97.822,"metro_code":0}, "status_code": 200}', 200)
    return mocked



def test_all(mock_file, mock_request):
    pytest.set_trace()
    results = LookUpController(mock_file, False, False).query()

    vars(results)
    assert results

