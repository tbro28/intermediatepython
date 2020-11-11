# content of test_sysexit.py
import pytest
from bitcoin-master import get_hash

def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()
