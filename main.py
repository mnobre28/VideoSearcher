from helpers.string_helper import StringHelper
from searchers.youtube_searcher import YoutubeSearcher
from settings import YOUTUBE_API_KEY, MAX_SEARCH_RESULTS

if __name__ == '__main__':
    search_term = "binaural beats"

    api = YoutubeSearcher(YOUTUBE_API_KEY)
    video_list = api.search(search_term, 200)

    #most_used_words_in_titles = StringHelper.get_most_used_words_from_text(video_list["all_titles"], 5)
    #most_used_words_in_descriptions = StringHelper.get_most_used_words_from_text(video_list["all_descriptions"], 5)

    l = ["VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY", "Kgc3u6nFjM0"] #, "nh76nar0TU8", u3oKJwzh6FA, SwDfco9Z19w, a9bC5NzhKk
    long_list = [
        "VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY",
        "VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY",
        "VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY",
        "VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY",
        "VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY",
        "VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY",
        "VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY",
        "VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY",
        "VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY",
        "VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY"
    ]
    two_hundred_lists = [
        "VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY",
        "VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY",
        "VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY",
        "VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY",
        "VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY",
        "VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY",
        "VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY",
        "VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY",
        "VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY",
        "VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY",
        "VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY",
        "VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY",
        "VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY",
        "VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY",
        "VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY",
        "VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY",
        "VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY",
        "VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY",
        "VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY",
        "VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY",
        "VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY",
        "VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY",
        "VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY",
        "VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY",
        "VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY",
        "VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY",
        "VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY",
        "VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY",
        "VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY",
        "VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY",
        "VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY",
        "VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY",
        "VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY",
        "VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY",
        "VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY",
        "VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY",
        "VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY",
        "VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY",
        "VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY",
        "VAwWdK7b2zE", "lUKGzvQj4bI", "lTmCZZr346I", "o1GJxVmYvE", "GZVbLEAhJJY"
    ]
    r = api.get_duration_of_videos(two_hundred_lists)

    #'PT7M14S'
    #'PT2H42M34S'
    pass
