from analyzers.word_counter import WordCounter


def test_can_convert_dict_list_to_string():
    dict_list = [
        {
            "key1": "qwerty1",
            "key2": "qwerty2"
        },
        {
            "key1": "asdfg1",
            "key2": "asdfg2"
        },
        {
            "key1": "zxcvb1",
            "key2": "zxcvb2"
        }
    ]
    expected_result = " {} {} {} ".format(dict_list[0]["key1"],
                                          dict_list[1]["key1"],
                                          dict_list[2]["key1"])

    final_string = WordCounter.convert_list_of_dicts_to_string(dict_list, "key1")
    assert final_string == expected_result
