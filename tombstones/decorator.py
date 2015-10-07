from __future__ import print_function
from __future__ import unicode_literals

import datetime
import inspect
import os

import wrapt

from tombstones.log import LogEntry
from tombstones.log import save_log_entry


def line_number_for_tombstone(lines, line_number):
    for line in lines:
        if line.strip() == "@tombstone":
            break
        line_number += 1
    return line_number


@wrapt.decorator
def tombstone(wrapped, instance, args, kwargs):
    """Tombstone decorator to save log entry."""
    save_log_entry(LogEntry(
        name=wrapped.__name__,
        source_file=os.path.abspath(
            inspect.getsourcefile(wrapped)
        ),
        line_number=line_number_for_tombstone(
            *inspect.getsourcelines(wrapped)
        ),
        datetime=str(datetime.datetime.now()),
    ))
    return wrapped(*args, **kwargs)
