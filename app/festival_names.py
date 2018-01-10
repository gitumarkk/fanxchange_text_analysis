import os

from base import Base


class FestivalNames(Base):
    def convert_list_to_first_word_frequency_list(self):
        """

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
        return { key: value for key, value in data.items() if len(value) > 1 }

    def get_unique_names(self):
        pass


if __name__ == '__main__':
    argv = sys.argv
    data_file_path = None

    if len(argv) > 1:
        data_file_path = argv[1]

    obj = WordCounter(data_file_path)
    print "Unique name: %s" % obj.get_total_words()


