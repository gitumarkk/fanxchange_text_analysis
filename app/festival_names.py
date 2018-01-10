import os

from base import Base


class FestivalNames(Base):
    def convert_list_to_first_word_frequency_list(self):
        """

        Returns:
            dict:
        """
        output = {}
        text_list = self.text_content.split('\n')

        for text in text_list:
            if not text:
                continue

            first_word = text.split()[0]
            if not output.get(first_word):
                output[first_word] = []
            output[first_word].append(text)
        return output

    def filter_non_repeating_names(self, data):
        """

        """
        return { key: value for key, value in data.items() if len(value) > 1 }

    def get_sentence_commonality(self, line_1, line_2):
        """
        Args:
            line_1 (str):
            line_2 (str):

        Returns:
            str:
        """
        festival_name = ''

        for index, char in enumerate(line_1):
            if line_1[index] != line_2[index]:
                return festival_name.strip()
            festival_name += line_1[index]

        return


    def build_festival_names(self, data):
        """
        Args:
            data (dict):

        Returns:
            list:
        """
        festival_name_list = []

        for key, value in data.items():
            festival_name = self.get_sentence_commonality(value[0], value[1])
            festival_name_list.append(festival_name)
        return festival_name_list

    def get_festival_names(self):
        """

        Returns:
            list:
        """
        data_all = convert_list_to_first_word_frequency_list()
        data_unique = filter_non_repeating_names()
        return self.build_festival_names(data_unique)


if __name__ == '__main__':
    argv = sys.argv
    data_file_path = None

    if len(argv) > 1:
        data_file_path = argv[1]

    obj = WordCounter(data_file_path)
    print "Unique names: %s" % obj.get_festival_names()


