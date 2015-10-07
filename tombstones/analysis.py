from __future__ import print_function

import json

from tombstones.log import FILENAME
from tombstones.log import LogEntry

def active_tombstones():
    log_entries = {}
    with open(FILENAME, 'r') as log_file:
        for line in log_file.readlines():
            log_entry = LogEntry(**json.loads(line.strip()))

            if log_entry.name not in log_entries:
                log_entries[log_entry.name] = log_entry
            else:
                log_entries[log_entry.name].datetime = log_entry.datetime
    print("Active tombstones")
    print("-----------------")
    for log_entry in log_entries.values():
        print(log_entry)
        print()
