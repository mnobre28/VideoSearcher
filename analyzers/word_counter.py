class WordCounter:
    def get_most_used_words_from_text(self, number_of_top_results, text_to_analyze):
        pass

    @staticmethod
    def convert_list_of_dicts_to_string(list_of_dicts, key_to_convert):
        final_string = ""
        for d in list_of_dicts:
            final_string += " " + d[key_to_convert] + " "
        return final_string
