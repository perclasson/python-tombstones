import mock
import pytest

from tombstones.log import LogEntry
from tombstones.log import save_log_entry

LOG_ENTRY_DATA = {
    "name": "name",
    "source_file": "source_file",
    "line_number": 1,
    "datetime": "datetime",
}


@pytest.fixture
def log_entry():
    return LogEntry(**LOG_ENTRY_DATA)


def test_log_entry_str(log_entry):
    print(log_entry)
    assert str(log_entry) == (
        "name in source_file at line number 1\n"
        "Last used at datetime"
    )


def test_log_entry_unique_id(log_entry):
    assert log_entry.unique_id == "source_file1"


def test_save_log_entry(log_entry):
    with mock.patch('tombstones.log.open', mock.mock_open()) as mock_open:
        save_log_entry(log_entry)
        assert mock_open.called
        mock_open.assert_has_calls([
            mock.call().write('\n')
        ])
