import mock
import pytest


@pytest.yield_fixture(autouse=True)
def mock_save_log_entry():
    patcher = mock.patch('tombstones.decorator.save_log_entry')
    yield patcher.start()
    patcher.stop()
