# Python
import os
import sys

# App
from base import Base


class FestivalNames(Base):
    def convert_text_content_to_first_word_dict(self):
        """Concerts the extracted text content into a dict

        Returns:
            dict: Contains the first word in the sentences as the key
            and sentences that has the first word in a values list
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
        """Used to narrow down on sentences where the first word has more than one occurences..

        Returns:
            dict: Contains keys of first word in sentences and values where
                the list has 2 or more items.

        """
        return { key: value for key, value in data.items() if len(value) > 1 }

    def get_sentence_commonality(self, line_1, line_2):
        """ First the first n characters where 2 sentences are the same. Assumes the whole
            sentence doesn't overlap hence there will not be an out of index error.

        Args:
            line_1 (str): Sentence 1
            line_2 (str): Sentence 2

        Returns:
            str | None: Where 2 sentences overlap, or none if there is no overlap
        """
        festival_name = ''

        for index, char in enumerate(line_1):
            if line_1[index] != line_2[index]:
                return festival_name.strip()
            festival_name += line_1[index]

        return


    def build_festival_names(self, data):
        """ Build festival names list where there list contains an overlap of first n
            characters between two sentences

        Args:
            data (dict): Contains key, valu dict where the keys are first words and values
                are a list of sentences

        Returns:
            list: List containing festival names
        """
        festival_name_list = []

        for key, value in data.items():
            festival_name = self.get_sentence_commonality(value[0], value[1])
            festival_name_list.append(festival_name)
        return festival_name_list

    def get_festival_names(self):
        """ A facade type function which allows festival names to be generated but hides
            the granular method calls.
        Returns:
            list: Contains the festival names
        """
        data_all = self.convert_text_content_to_first_word_dict()
        data_unique = self.filter_non_repeating_names(data_all)
        return self.build_festival_names(data_unique)


if __name__ == '__main__':
    argv = sys.argv
    data_file_path = None

    if len(argv) > 1:
        data_file_path = argv[1]

    obj = FestivalNames(data_file_path)
    print "The Festivals are:\n%s" % "\n".join(obj.get_festival_names())


