import pytest

from helpers.time_helper import TimeHelper


@pytest.mark.parametrize("time_in_iso, time_in_minutes", (("PT7M14S", 7), ("PT2H42M34S", 163)))
def test_can_convert_iso_to_minutes(time_in_iso, time_in_minutes):
    result = TimeHelper.convert_iso_to_minutes(time_in_iso)
    assert time_in_minutes == result
