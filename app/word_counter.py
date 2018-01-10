# Python
import os
import sys
from collections import Counter

from base import Base


class WordCounter(Base):
    def __init__(self, data_file_path=None):
        super(WordCounter, self).__init__(data_file_path)

    def get_total_words(self):
        """Returns the total number of words in the given content

        Returns:
            int: The total words
        """
        return len(self.text_content.split())

    def get_most_common_words(self, limit=10):
        """Returns the total number of words in the given content

        Args:
            limit (int): Optional variable for most common words

        Returns:
            list: A list containing most common words based on the limit
        """

        counter_obj = Counter(self.text_content.split())
        return counter_obj.most_common(limit)


if __name__ == '__main__':
    argv = sys.argv
    data_file_path = None

    if len(argv) > 1:
        data_file_path = argv[1]

    obj = WordCounter(data_file_path)
    print "The word count is: %s" % obj.get_total_words()
    print "The most frequent words are: %s" % obj.get_most_common_words()

