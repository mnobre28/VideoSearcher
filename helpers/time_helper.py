import pandas


class TimeHelper:
    @staticmethod
    def convert_iso_to_minutes(time_in_iso):
        timedelta = pandas.Timedelta(time_in_iso)
        time_in_minutes = round(timedelta.total_seconds() / 60)
        return time_in_minutes
