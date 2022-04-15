import pytest

from helpers.string_helper import StringHelper


@pytest.fixture
def list_of_words():
    return "amusement selective tall sound didactic unkempt selective " \
           "tall sound glass distance didactic actor selective tall sound " \
           "glass distance didactic faint"


def test_can_get_most_common_words(list_of_words):
    results = StringHelper.get_most_used_words_from_text(list_of_words, 5)
    assert results == ['selective', 'tall', 'sound', 'didactic', 'glass']
