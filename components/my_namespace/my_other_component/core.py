from my_namespace.my_component import DataBase

import inspect
from pathlib import Path

def my_func():
    # inspect.stack()[1] is the caller's frame
    caller_frame = inspect.stack()[1]
    caller_path = Path(caller_frame.filename)
    print("Called from:", caller_path.resolve())

def my_ll_func():
    frame = inspect.stack()[1]
    # Python 3.5+: you can also use frame.filename
    caller_file = frame[0].f_code.co_filename
    caller_path = Path(caller_file).resolve()
    print("Called from:", caller_path)

my_func()
# my_ll_func()
# breakpoint()
class SilverBriDB(DataBase, run_init=True):
    """Base class to serve as a namespace DB/schema for all the Silver BRI Tables.

    Args:
        DataModel (class): The base class from which it inherits.

    """

    __abstract__ = True
    
