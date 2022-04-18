from helpers.input_helper import InputHelper
from helpers.string_helper import StringHelper
from helpers.time_helper import TimeHelper
from searchers.youtube_searcher import YoutubeSearcher
from settings import YOUTUBE_API_KEY, MAX_SEARCH_RESULTS

if __name__ == '__main__':
    print("Enter youtube api key (leave empty for default)")
    api_key = input()
    print("Enter search words:")
    search_term = input()
    print("Enter daily watch time in minutes (example: 10, 10, 10, 10, 10, 10, 10):")
    daily_watch_time = InputHelper.format_watch_time(input())

    print("Searching, please wait...")
    api = YoutubeSearcher(YOUTUBE_API_KEY if api_key == "" else api_key)
    video_list = api.search(search_term, MAX_SEARCH_RESULTS)

    print("======")
    most_used_words_in_titles = StringHelper.get_most_used_words_from_text(video_list["all_titles"], 5)
    print("Most commonly used words in titles: " + str(most_used_words_in_titles))
    most_used_words_in_descriptions = StringHelper.get_most_used_words_from_text(video_list["all_descriptions"], 5)
    print("Most commonly used words in descriptions: " + str(most_used_words_in_descriptions))
    video_durations = api.get_duration_of_videos(video_list["all_video_ids"])
    days_to_watch = TimeHelper.get_days_needed_to_watch_all_videos(daily_watch_time, video_durations)
    print("Days required to watch all videos: " + str(days_to_watch))

    print("Show all video information? Y/N")
    response = input()
    if response == "Y" or response == "y":
        for description in video_list["complete_video_description"]:
            print(description)
