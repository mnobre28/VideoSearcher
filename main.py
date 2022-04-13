from helpers.string_helper import StringHelper
from searchers.youtube_searcher import YoutubeSearcher
from settings import YOUTUBE_API_KEY, MAX_SEARCH_RESULTS

if __name__ == '__main__':
    search_term = "pound cake"

    api = YoutubeSearcher(YOUTUBE_API_KEY)
    video_list = api.search(search_term, 10)
    title_list = StringHelper.convert_list_of_dicts_to_string(video_list, "title")
    description_list = StringHelper.convert_list_of_dicts_to_string(video_list, "description")

    most_used_words_in_titles = StringHelper.get_most_used_words_from_text(title_list, 5)
    most_used_words_in_descriptions = StringHelper.get_most_used_words_from_text(description_list, 5)

    pass
