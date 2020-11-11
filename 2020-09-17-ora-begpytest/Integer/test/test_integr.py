import integr
import pytest

def test_basic():
    res = integr.parse('1,3,5,9')
    assert res == [1, 3, 5, 9]

@pytest.mark.wrong
def test_bad1():
    with pytest.raises(ValueError):
        integr.parse('bad_input')

@pytest.mark.xfail(raises=ValueError)
@pytest.mark.wrong
def test_bad2():
    res = integr.parse('1-3,12-15')

if __name__ == '__main__':
    pytest.main()
