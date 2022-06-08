import pytest
from unittest.mock import MagicMock
from tools.releases import fetch_release_info


def test_fetch_release_info_returns_ReleaseInfo_On_Success(
        requests_get_mock: MagicMock):
    fetch_release_info('latest')

    requests_get_mock.assert_called_once()
    assert requests_get_mock.call_args_list[0].endswith('/latest')



def test_fetch_release_info_raises_RuntimeError_on_fetch_error(
        requests_get_mock: MagicMock):
    requests_get_mock.return_value.raise_for_status.side_effect = IOError(
        "Server error")

    with pytest.raises(RuntimeError):
        fetch_release_info('latest')

    requests_get_mock.assert_called_once()
    assert requests_get_mock.call_args_list[0].endswith('/latest')
