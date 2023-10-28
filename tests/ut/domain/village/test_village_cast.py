import pytest

from exceptions.exceptions import IllegalArgumentsException
from src.domain.village.village_cast import VillageCast


class TestVillageCast:
    @pytest.mark.parametrize(
        "actual",
        [(""), ("a"), (None)],
    )
    def test_of_error(self, actual):
        with pytest.raises(IllegalArgumentsException):
            VillageCast.of(actual)

    @pytest.mark.parametrize(
        "actual, expected",
        [
            ("A", VillageCast.A),
            ("B", VillageCast.B),
            ("C", VillageCast.C),
            ("D", VillageCast.D),
            ("Z", VillageCast.Z),
        ],
    )
    def test_of(self, actual, expected):
        assert VillageCast.of(actual) is expected
