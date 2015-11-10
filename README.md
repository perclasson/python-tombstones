# Tombstones
[![Build Status](https://travis-ci.org/perclasson/python-tombstones.svg?branch=master)](https://travis-ci.org/perclasson/python-tombstones)
[![Coverage Status](https://coveralls.io/repos/perclasson/python-tombstones/badge.svg?branch=master&service=github)](https://coveralls.io/github/perclasson/python-tombstones?branch=master)

Python package to mark code that you suspect is unreachable or dead.

# Installation
To install the package:

```shell
$ pip install tombstones
```

# Usage
If you believe a function, class or method is never used, mark it with a tombstone.
```python
from tombstones import tombstone

@tombstone
def example_function():
    pass

@tombstone
class ExampleClass(object):
    pass

class AnotherExampleClass(object):
    @tombstone
    def example_method(self):
        pass
```

If your tombstone is ever executed, it will save to an entry log file, which you can read with the following command:
```shell
$ tombstones active
```
You can then remove any active tombstones, as they're not marking dead code.
```shell
Active tombstones
-----------------
example_function in test_decorator.py at line number 3
Last used at 2015-10-07 16:14:18
```
