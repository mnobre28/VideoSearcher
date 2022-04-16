from pyyoutube import Api

from helpers.string_helper import StringHelper
from helpers.time_helper import TimeHelper
from searchers.generic_searcher import GenericSearcher


class YoutubeSearcher(GenericSearcher):
    def __init__(self, api_key):
        self.api_connection = Api(api_key=api_key)

    def search(self, search_term, max_results=200):
        result = self.api_connection.search(q=search_term,
                                            search_type="video",
                                            count=max_results)
        formatted_result = self.format_search_result(result)
        return formatted_result

    def get_duration_of_videos(self, video_ids):
        result = self.api_connection.get_video_by_id(video_id=video_ids)
        video_durations = self.format_video_durations(result)
        return video_durations

    @staticmethod
    def format_search_result(search_result):
        video_data = {
            "all_titles": "",
            "all_descriptions": "",
            "all_durations": [],
            "all_video_ids": [],
            "complete_video_description": [],
        }
        for video in search_result.items:
            video_data["all_titles"] += \
                StringHelper.remove_punctuation_from_string(video.snippet.title) + " "
            video_data["all_descriptions"] += \
                StringHelper.remove_punctuation_from_string(video.snippet.description) + " "
            video_data["all_video_ids"].append(video.id.videoId)
            video_data["complete_video_description"] = {
                "video_title": video.snippet.title,
                "video_description": video.snippet.description,
                "video_id": video.id.videoId
            }
        return video_data

    @staticmethod
    def format_video_durations(search_result):
        all_durations = []
        for video in search_result.items:
            video_duration_in_minutes = TimeHelper.convert_iso_to_minutes(video.contentDetails.duration)
            all_durations.append(video_duration_in_minutes)
        return all_durations
