import json

from pkg_resources import resource_filename
from collections import namedtuple

FILENAME = resource_filename('tombstones', 'tombstones.log')


class LogEntry(namedtuple(
    'LogEntry',
    ['name', 'source_file', 'line_number', 'datetime']
)):
    def __str__(self):
        return (
            "{name} in {source_file} at line number {line_number}\n"
            "Last used at {datetime}"
        ).format(**self._asdict())

    @property
    def unique_id(self):
        return self.source_file + str(self.line_number)


def save_log_entry(entry):
    with open(FILENAME, 'a') as log_file:
        json.dump(entry._asdict(), log_file)
        log_file.write('\n')
