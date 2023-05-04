# Background

This code tries to reproduce https://github.com/googleapis/google-auth-library-python/issues/1264.

# How to run

**Note:** I've only tested this a Ubuntu flavor.

## Set up a Python environment

```
$ python -m venv env && source env/bin/activate
$ python -m pip install google-auth requests
$ ./repro.sh
```
The credentials should not be expired if the timezone has changed.

If the credentials were forcefully made to expire, then they should not remain valid across tiemzones.
