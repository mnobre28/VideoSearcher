import pytest

from helpers.string_helper import StringHelper


@pytest.fixture
def basic_dict_list():
    return [
        {
            "key1": "amusement selective tall sound didactic unkempt",
            "key2": "wrong key!"
        },
        {
            "key1": "selective tall sound glass distance didactic actor",
            "key2": "wrong key!"
        },
        {
            "key1": "selective tall sound glass distance didactic faint",
            "key2": "wrong key!"
        }
    ]


@pytest.fixture
def special_dict_list():
    return [
        {
            "key1": "amusement!! selective tall! sound? didactic??? unkempt",
            "key2": "wrong key!"
        },
        {
            "key1": "selective.... tall.. glass. distance;;; didactic, actor;",
            "key2": "wrong key!"
        },
        {
            "key1": "selective::: tall sound ;glass distance; didactic: faint?",
            "key2": "wrong key!"
        }
    ]


@pytest.fixture
def list_of_words():
    return "amusement selective tall sound didactic unkempt selective " \
           "tall sound glass distance didactic actor selective tall sound " \
           "glass distance didactic faint"


def test_can_convert_dict_list_to_string(basic_dict_list):

    expected_result = "{} {} {} ".format(basic_dict_list[0]["key1"],
                                         basic_dict_list[1]["key1"],
                                         basic_dict_list[2]["key1"])

    converted_string = StringHelper.convert_list_of_dicts_to_string(basic_dict_list, "key1")
    assert converted_string == expected_result


def test_can_convert_dict_list_to_string_without_special_characters(basic_dict_list, special_dict_list):
    expected_result = "{} {} {} ".format(basic_dict_list[0]["key1"],
                                         basic_dict_list[1]["key1"],
                                         basic_dict_list[2]["key1"])

    converted_string = StringHelper.convert_list_of_dicts_to_string(special_dict_list, "key1")
    assert converted_string == expected_result


def test_can_get_most_common_words(list_of_words):
    results = StringHelper.get_most_used_words_from_text(list_of_words, 5)
    assert results == ['selective', 'tall', 'sound', 'didactic', 'glass']
