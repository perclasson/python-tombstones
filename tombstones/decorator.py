from __future__ import print_function
from __future__ import unicode_literals

import datetime
import inspect
import os
import json

import wrapt

from pkg_resources import resource_filename


def log_entry(entry):
    filename = resource_filename('tombstones', 'tombstones.log')
    with open(filename, 'a') as log_file:
        json.dump(entry, log_file)
        log_file.write('\n')


def line_number_for_tombstone(wrapped):
    lines, line_number = inspect.getsourcelines(wrapped)
    for line in lines:
        if line.strip() != "@tombstone":
            line_number += 1
    return line_number


@wrapt.decorator
def tombstone(wrapped, instance, args, kwargs):
    """Tombstone decorator to save log entry."""
    entry = dict(
        name=wrapped.__name__,
        source_file=os.path.abspath(inspect.getsourcefile(wrapped)),
        line_number=line_number_for_tombstone(wrapped),
        datetime=str(datetime.datetime.now()),
    )
    log_entry(entry)
    return wrapped(*args, **kwargs)
