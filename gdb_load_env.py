# Inspired from https://github.com/chrisc11/gdb-python-scripts/blob/master/gdb_newlib.py
try:
    import gdb
except ImportError:
    error_str = """
    This script can only be run within gdb!
    You need to 'source gdb_load_env.py' from (gdb) or in your init file
    """
    raise Exception(error_str)


class LoadEnvFile(gdb.Command):
  """Sets the current environment from contents of a .env file"""
  def __init__(self):
    super(LoadEnvFile, self).__init__("load-env-file", gdb.COMMAND_USER)

  def invoke(self, arg, from_tty):
    # FIXME: If specified arg is a directory, try to find a '.env' file in it.
    with open(arg, 'r') as f:
      for line in f.readlines():
        gdb.execute('set environment {}'.format(line), from_tty, True)

LoadEnvFile()
