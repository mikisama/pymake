pymake + python 3 patches
=========================

[![Build Status](https://travis-ci.com/fcostin/pymake.svg?branch=master)](https://travis-ci.com/fcostin/pymake)

Fork of [https://github.com/mozilla/pymake](https://github.com/mozilla/pymake)

### What is pymake?

>	make.py (and the pymake modules that support it) are an implementation of the make tool
>	which are mostly compatible with makefiles written for GNU make.

Please refer to [`ORIGINAL_README`](/ORIGINAL_README) and [`LICENSE`](/LICENSE)

### Why fork pymake?

Attempt to get pymake running under Python 3, with a stable test suite.

### Will this forked version of pymake still run in Python 2?

No.

### Development: running the test suite

Prerequisites:

*	default `python` is Python 3
*	[pytest](https://docs.pytest.org) installed (`pip install -r test-requirements.txt`)
*	a dev install of `pymake` package in this repo (`pip install -e .`)
*	GNU Make installed to test against (assumed to be named `gmake`, can be overridden)

With [pytest](https://docs.pytest.org) installed, the test suite can be run from the root directory of this repo as follows:

```
pytest --gmake=make .
```

With the optional `pytest-dist` plugin installed, the tests can be run in parallel. For example, to use 8 CPUs:

```
pytest --gmake=make -n 8 .
```

This gives about a 5x speedup on my machine.
