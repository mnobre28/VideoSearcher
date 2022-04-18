

class InputHelper:
    @staticmethod
    def format_watch_time(user_input):
        watch_time_list = [int(s) for s in user_input.split(',')]
        return watch_time_list
