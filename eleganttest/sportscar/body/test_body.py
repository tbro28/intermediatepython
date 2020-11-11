import pytest
from pytest import mark

@mark.body
class BodyTests:

    @mark.smoke
    def test_pass(self):
        assert True

    def test_door(self):
        assert True

    def test_windshield(self):
        assert True