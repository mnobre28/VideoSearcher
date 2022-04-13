from searchers.youtube_searcher import YoutubeSearcher
from settings import YOUTUBE_API_KEY, MAX_SEARCH_RESULTS

if __name__ == '__main__':
    search_term = "pound cake"

    api = YoutubeSearcher(YOUTUBE_API_KEY)
    search_result = api.search(search_term, 2)
    pass
