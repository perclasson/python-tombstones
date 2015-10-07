from __future__ import print_function
import fnmatch
import inspect
import os
import sys
import pkgutil

def find_tombstones(dirname):
    for importer, name, ispkg in pkgutil.iter_modules([dirname]):
        try:
            module = importer.find_module(name).load_module(name)

            classes = inspect.getmembers(module, inspect.isclass)
            methods = inspect.getmembers(module, inspect.ismethod)
            functions = inspect.getmembers(module, inspect.isfunction)

            tombstones = [fn for _, fn in inspect.getmembers(module) if hasattr(fn, '__tombstone__')]
            print("tombstones", [t.__name__ for t in tombstones])
        except:
            print("Could not load {}.".format(name))
