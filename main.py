from helpers.string_helper import StringHelper
from searchers.youtube_searcher import YoutubeSearcher
from settings import YOUTUBE_API_KEY, MAX_SEARCH_RESULTS

if __name__ == '__main__':
    search_term = "binaural beats"
    daily_watch_time = [10, 10, 10, 10, 10, 10, 10]

    api = YoutubeSearcher(YOUTUBE_API_KEY)
    video_list = api.search(search_term, 200)

    most_used_words_in_titles = StringHelper.get_most_used_words_from_text(video_list["all_titles"], 5)
    most_used_words_in_descriptions = StringHelper.get_most_used_words_from_text(video_list["all_descriptions"], 5)
    # -> this only fetches in batches of 50
    r = api.get_duration_of_videos(video_list["all_video_ids"][:50])

    pass
