from unittest.mock import Mock

from searchers.youtube_searcher import YoutubeSearcher


def create_mock_video_data(title, description, video_id):
    video_data = Mock()
    video_data.snippet.title = title
    video_data.snippet.description = description
    video_data.id.videoId = video_id
    return video_data


def test_can_convert_youtube_response_to_new_format():
    all_video_data = [
        create_mock_video_data("first title!", "first description;", "123"),
        create_mock_video_data("second title?", "second description;", "456"),
        create_mock_video_data("third title!", "third description;", "789"),
    ]

    youtube_response = Mock()
    youtube_response.items = all_video_data

    result = YoutubeSearcher.format_search_result(youtube_response)
    assert result["all_titles"] == "first title second title third title "
    assert result["all_descriptions"] == "first description second description third description "
    assert result["all_video_ids"] == ["123", "456", "789"]
