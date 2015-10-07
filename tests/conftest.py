import mock
import pytest


@pytest.yield_fixture(autouse=True)
def mock_log_open():
    patcher = mock.patch('tombstones.log.open', mock.mock_open())
    yield patcher.start()
    patcher.stop()
