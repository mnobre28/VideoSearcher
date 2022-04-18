from helpers.string_helper import StringHelper
from helpers.time_helper import TimeHelper
from searchers.youtube_searcher import YoutubeSearcher
from settings import YOUTUBE_API_KEY, MAX_SEARCH_RESULTS

if __name__ == '__main__':
    search_term = "pound cake"
    daily_watch_time = [20, 40, 30, 15, 40, 20, 30]

    api = YoutubeSearcher(YOUTUBE_API_KEY)
    video_list = api.search(search_term, MAX_SEARCH_RESULTS)

    most_used_words_in_titles = StringHelper.get_most_used_words_from_text(video_list["all_titles"], 5)
    most_used_words_in_descriptions = StringHelper.get_most_used_words_from_text(video_list["all_descriptions"], 5)
    r = api.get_duration_of_videos(video_list["all_video_ids"])
    days_to_watch = TimeHelper.get_days_needed_to_watch_all_videos(daily_watch_time, r)

    pass
