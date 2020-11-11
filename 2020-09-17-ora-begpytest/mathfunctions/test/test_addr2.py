# content of test_sysexit.py
import pytest
# some_file.py
import sys

# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'C:\\Users\Tim\\python'
                   '\intermediate'
                   '\\2020-09-17-ora-begpytest\\mathfunctions')
sys.path.insert(1, '../mathfunctions')




def test_add():
    res = addr(2, 3)
    assert res == 5
