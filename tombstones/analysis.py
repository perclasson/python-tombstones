from __future__ import print_function

import json

from tombstones.log import FILENAME
from tombstones.log import LogEntry

def unique_log_entries():
    log_entries = {}
    try:
        with open(FILENAME, 'r') as log_file:
            for line in log_file.readlines():
                log_entry = LogEntry(**json.loads(line.strip()))
                unique_identifier = log_entry.source_file + str(log_entry.line_number)
                if log_entry.name not in log_entries:
                    log_entries[unique_identifier] = log_entry
                else:
                    log_entries[unique_identifier].datetime = log_entry.datetime
    except IOError:
        pass
    return log_entries

def active_tombstones():
    log_entries = unique_log_entries()
    if not log_entries:
        print("No active tombstones")
        return
    print("Active tombstones")
    print("-----------------")
    for log_entry in log_entries.values():
        print(log_entry)
        print()
