import json

from pkg_resources import resource_filename
from collections import namedtuple
from collections import OrderedDict

FILENAME = resource_filename('tombstones', 'tombstones.log')


class LogEntry(namedtuple(
    'LogEntry',
    ['name', 'source_file', 'line_number', 'datetime']
)):
    def __str__(self):
        return (
            "{name} in {source_file} at line number {line_number}\n"
            "Last used at {datetime}"
        ).format(**self.as_dict())

    @property
    def unique_id(self):
        return self.source_file + str(self.line_number)

    def as_dict(self):
        return OrderedDict(zip(self._fields, self))


def save_log_entry(entry):
    with open(FILENAME, 'a') as log_file:
        json.dump(entry.as_dict(), log_file)
        log_file.write('\n')
