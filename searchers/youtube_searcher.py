from pyyoutube import Api

from searchers.generic_searcher import GenericSearcher


class YoutubeSearcher(GenericSearcher):
    def __init__(self, api_key):
        self.api_connection = Api(api_key=api_key)

    def search(self, search_term, max_results=200):
        result = self.api_connection.search(q=search_term,
                                            search_type="video",
                                            count=max_results)
        formatted_result = self._format_search_result(result)
        return formatted_result

    @staticmethod
    def _format_search_result(search_result):
        list_of_video_data = []
        for video in search_result.items:
            video_data = {
                "title": video.snippet.title,
                "description": video.snippet.description,
                "id": video.id.videoId
            }
            list_of_video_data.append(video_data)
        return list_of_video_data
