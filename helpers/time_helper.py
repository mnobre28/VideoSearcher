import pandas


class TimeHelper:
    @staticmethod
    def convert_iso_to_minutes(time_in_iso):
        timedelta = pandas.Timedelta(time_in_iso)
        time_in_minutes = round(timedelta.total_seconds() / 60)
        return time_in_minutes

    @staticmethod
    def get_days_needed_to_watch_all_videos(daily_watch_time, video_durations):
        longest_watch_time = max(daily_watch_time)
        video_durations = TimeHelper.remove_video_durations_longer_than_limit(longest_watch_time, video_durations)
        daily_watch_time_index = 0
        index = 0
        days_required = 0
        while index < len(video_durations):
            index = TimeHelper.watch_videos_for_a_day(daily_watch_time[daily_watch_time_index], video_durations, index)
            daily_watch_time_index += 1
            if daily_watch_time_index > 4:
                daily_watch_time_index = 0
            days_required += 1
        return days_required

    @staticmethod
    def watch_videos_for_a_day(watch_time_limit, video_durations, index=0):
        current_video_duration = video_durations[index]

        while watch_time_limit >= current_video_duration and index < len(video_durations):
            watch_time_limit -= current_video_duration
            index += 1
            if index < len(video_durations):
                current_video_duration = video_durations[index]
        return index

    @staticmethod
    def remove_video_durations_longer_than_limit(limit, video_durations):
        new_list = []
        for video_duration in video_durations:
            if video_duration < limit:
                new_list.append(video_duration)
        return new_list
