import pytest

from helpers.time_helper import TimeHelper


@pytest.mark.parametrize("daily_watch_time, video_durations, expected_days_to_watch",
                         (([20, 10, 20, 15, 30], [10, 5, 15, 5, 5], 4),
                          ([20, 10, 20, 15, 30], [10, 5, 15, 20, 20, 40], 6),
                          ([20, 10, 20, 15, 30], [10, 5, 15, 5, 20, 30, 5, 45, 10, 35, 10, 20, 10, 15, 10, 25, 20, 10,
                                                  15, 5, 15, 45, 20, 25, 5], 25)))
def test_can_return_time_to_watch_videos(daily_watch_time, video_durations, expected_days_to_watch):
    days_to_watch = TimeHelper.get_days_needed_to_watch_all_videos(daily_watch_time, video_durations)
    assert days_to_watch == expected_days_to_watch


@pytest.mark.parametrize("time_in_iso, time_in_minutes",
                         (("PT7M14S", 7),
                          ("PT2H42M34S", 163)))
def test_can_convert_iso_to_minutes(time_in_iso, time_in_minutes):
    result = TimeHelper.convert_iso_to_minutes(time_in_iso)
    assert time_in_minutes == result


@pytest.mark.parametrize("watch_time_limit, video_durations, expected_index",
                         ((30, [5, 15, 40, 25], 2),
                          (30, [5, 40, 99, 15, 25, 29], 2)))
def test_can_watch_videos_within_daily_limit(watch_time_limit, video_durations, expected_index):
    video_durations = TimeHelper.remove_video_durations_longer_than_limit(watch_time_limit, video_durations)
    index = TimeHelper.watch_videos_for_a_day(watch_time_limit, video_durations)
    assert index == expected_index
