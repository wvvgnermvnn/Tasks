# import pandas as pd
# import numpy as np
# data = pd.read_csv('mlcourse_open/data/telecom_churn.csv')
# print(data.describe())

"""Usage: parse-args --number=<int> [--flag]"""
import inspect
import functools
import sys

def simple_cli(description):
    """Implement a simple annotation-based command-line parser."""
    def decorator(main):
        @functools.wraps(main)
        def wrapper(argv=None):
            if argv is None:
                argv = sys.argv
            if '--help' in argv:
                sys.exit(description)
            params = inspect.signature(main).parameters
            parser = ArgumentParser.from_params(*params.values())
            try:
                return main(**parser.parse_args(argv[1:]))
            except ArgumentError as e:
                sys.exit(f"Error: {e}\n{description}")
        return wrapper
    return decorator