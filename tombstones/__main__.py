from __future__ import print_function

import sys

from tombstones.analysis import active_tombstones

ALL_COMMANDS = {}


def command(name):
    def wrapper(wrapped):
        ALL_COMMANDS[name] = wrapped
        return wrapped
    return wrapper


@command('help')
def help(args):
    print('Usage: tombstones command [options]', end='')
    print()
    print('Available commands are:')

    for name in ALL_COMMANDS:
        print(name)


@command('active')
def active(args):
    active_tombstones()


def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    if args:
        command = args[0]
    else:
        command = 'help'

    if command not in ALL_COMMANDS:
        print("Unknown command '{}'. Type 'tombstones help' for usage.".format(
            command))
        return
    return ALL_COMMANDS[command](args[1:])

if __name__ == '__main__':
    main()
