"""Provides fake data from GitHub response calls.

Example data taken directly from real calls to GitHub API documentation:
https://docs.github.com/en/rest/releases/releases
"""
import pytest
from pytest_mock import MockerFixture


@pytest.fixture
def requests_get_mock(mocker: MockerFixture):
    requests_get_mock = mocker.patch("tools.releases.requests.get")
    response_mock = mocker.patch("requests.Response", autospec=True)
    requests_get_mock.return_value = response_mock

    return requests_get_mock


def mock_requests_get(mocker: MockerFixture, request_raises_error: bool):
    """Mock out a requests get to return a mock Response

    :param mocker: pytest_mock fixture with access to the mock api
    :param request_raises_error: If True Response.raise_for_status raises an exception
                                 else a .json return value is set
    :return: A mocked out requests.get object
    """
    requests_get_mock = mocker.patch("tools.releases.requests.get")
    response_mock = mocker.patch("requests.Response", autospec=True)
    if request_raises_error:
        response_mock.raise_for_status.side_effect = IOError("Server error")
    else:
        response_mock.json.return_value = _create_release_response_payload()
    requests_get_mock.return_value = response_mock

    return requests_get_mock


def _create_release_response_payload():
    return {"tag_name": "v6.3.0", "published_at": "2022-02-08T15:13:30Z"}
