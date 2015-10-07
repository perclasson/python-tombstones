import mock

import json

from tombstones.analysis import unique_log_entries
from tombstones.analysis import active_tombstones
from tombstones.log import LogEntry

FIRST_LOG_ENTRY = LogEntry(**{
    "name": "first_function",
    "source_file": "test_decorator.py",
    "line_number": 16,
    "datetime": "2015-10-07 16:14:18.965741",
})
SECOND_LOG_ENTRY = LogEntry(**{
    "name": "second_function",
    "source_file": "test_decorator.py",
    "line_number": 20,
    "datetime": "2015-10-08 16:14:18.965741",
})

FIRST_JSON_ENTRY = json.dumps(FIRST_LOG_ENTRY._asdict())
SECOND_JSON_ENTRY = json.dumps(SECOND_LOG_ENTRY._asdict())

FIRST_TWICE_AS_JSON_ENTRIES = '\n'.join([
    FIRST_JSON_ENTRY]*2,
)
FIRST_AND_SECOND_AS_JSON_ENTRIES = '\n'.join(
    [FIRST_JSON_ENTRY, SECOND_JSON_ENTRY]
)


@mock.patch('tombstones.analysis.open', mock.mock_open(
    read_data=FIRST_JSON_ENTRY
))
def test_first_log_entry():
    assert len(unique_log_entries()) == 1


@mock.patch('tombstones.analysis.open', mock.mock_open(
    read_data=SECOND_JSON_ENTRY
))
def test_second_log_entry():
    assert len(unique_log_entries()) == 1


@mock.patch('tombstones.analysis.open', mock.mock_open(
    read_data=FIRST_TWICE_AS_JSON_ENTRIES
))
def test_first_twice_log_entry():
    assert len(unique_log_entries()) == 1


@mock.patch('tombstones.analysis.open', mock.mock_open(
    read_data=FIRST_AND_SECOND_AS_JSON_ENTRIES
))
def test_first_and_second_log_entry():
    assert len(unique_log_entries()) == 2


@mock.patch('tombstones.analysis.unique_log_entries')
@mock.patch('tombstones.analysis.print')
def test_active_tombstones(mock_print, mock_log_entries):
    mock_log_entries.return_value = {
        FIRST_LOG_ENTRY.unique_id: FIRST_LOG_ENTRY
    }

    active_tombstones()
    assert mock_print.called
    mock_print.has_calls([
        mock.call("Active tombstones"),
        mock.call("-----------------"),
        mock.call(str(FIRST_LOG_ENTRY)),
    ])


@mock.patch('tombstones.analysis.unique_log_entries')
@mock.patch('tombstones.analysis.print')
def test_no_active_tombstones(mock_print, mock_log_entries):
    mock_log_entries.return_value = {}

    active_tombstones()
    assert mock_print.called
    mock_print.assert_called_with("No active tombstones")
