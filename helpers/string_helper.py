import string
from collections import Counter


class StringHelper:
    @staticmethod
    def get_most_used_words_from_text(text_to_analyze, number_of_top_results):
        split_text = text_to_analyze.split()
        counters_found = Counter(split_text)
        occurrences = counters_found.most_common(number_of_top_results)
        list_of_top_occurrences = []
        for occurrence in occurrences:
            list_of_top_occurrences.append(occurrence[0])
        return list_of_top_occurrences

    @staticmethod
    def convert_list_of_dicts_to_string(list_of_dicts, key_to_convert, delimiter=" "):
        final_string = ""
        for d in list_of_dicts:
            final_string += d[key_to_convert] + delimiter
        final_string = StringHelper.remove_punctuation_from_string(final_string)
        return final_string

    @staticmethod
    def remove_punctuation_from_string(string_to_convert):
        converted_string = string_to_convert.translate(str.maketrans('', '', string.punctuation))
        return converted_string
