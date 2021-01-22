# gdb-load-env-file
Sets environment variables for the current execution from a .env file.

It is intended to be used for debugging python modules written in C or C++
(and possibly other compiled languages that are also debuggable in gdb) that
need a set of custom environment variables.

# Usage
Either start debugging session with this script loaded:
```
$ gdb -ex "source path-to-gdb_load_env.py" \
  -ex "load-env-file path-to-env-file" \
  --args python ...
```
or load environment variables from gdb console:
```
$ gdb --args python ...
...
(gdb) source path-to-gdb_load_env.py
(gdb) load-env-file /path/to/.env
```
