import mock

from tombstones import tombstone
from tombstones.decorator import line_number_for_tombstone


def test_tombstone_decorator():
    def function(test_value):
        return test_value

    decorated_func = tombstone(function)
    assert decorated_func == function


def test_save_log_entry(mock_save_log_entry):
    @tombstone
    def function():
        pass
    function()
    assert mock_save_log_entry.called


@mock.patch('tombstones.decorator.LogEntry')
@mock.patch('datetime.datetime')
def test_log_entry_arguments(mock_datetime, mock_log_entry):
    now = str(mock.MagicMock())
    mock_datetime.now.return_value = now

    @tombstone
    def test_function():
        pass
    test_function()

    assert mock_log_entry.called
    mock_log_entry.assert_called_with(
        name='test_function',
        line_number=29,
        datetime=now,
        source_file=__file__,
    )


def test_first_line_number_for_tombstone():
    lines = [
        '    @tombstone\n',
        '    def test_function():\n',
        '        pass\n'
    ]
    line_number = 1
    assert line_number_for_tombstone(lines, line_number) == line_number


def test_second_line_number_for_tombstone():
    lines = [
        '    @test\n',
        '    @tombstone\n',
        '    def test_function():\n',
        '        pass\n'
    ]
    line_number = 1
    assert line_number_for_tombstone(lines, line_number) == line_number + 1
