# flake8: noqa
import os
import sys

if sys.version_info[:2] >= (3, 0):
    def exec_file_wrapper(fpath, g_vars, l_vars):
        with open(fpath) as f:
            code = compile(f.read(), os.path.basename(fpath), 'exec')
            try:
                exec(code, g_vars, l_vars)
            except Exception as e:
                print(f"Error executing code: {e}")
                # Handle the error appropriately
