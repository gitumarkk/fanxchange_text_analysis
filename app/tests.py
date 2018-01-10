# Python
import unittest


# App
from base import Base
from word_counter import WordCounter
from festival_names import FestivalNames


class TestBase(unittest.TestCase):
    def test_initialize_base_has_default_content(self):
        obj = Base()
        self.assertIn('Lady Gaga', obj.text_content)


class TestWordCount(unittest.TestCase):
    def setUp(self):
        self.content = "One Two Two Three Three Three Four Four Four Four"

    def test_initialize_word_count_has_default_content(self):
        obj = WordCounter()

        self.assertIn('Lady Gaga', obj.text_content)

    def test_get_total_words(self):
        obj = WordCounter()
        obj.text_content = self.content
        self.assertEqual(obj.get_total_words(), 10)

    def test_get_most_common_words(self):
        obj = WordCounter()
        obj.text_content = self.content
        self.assertEqual(
            obj.get_most_common_words(2),
            [('Four', 4), ('Three', 3)]
        )


class TestFestivalNames(unittest.TestCase):
    def setUp(self):
        self.content = "One Two Two Three Three Three Four Four Four Four"

    def test_initialize_word_count_has_default_content(self):
        obj = FestivalNames()
        self.assertIn('Lady Gaga', obj.text_content)

    def test_convert_list_to_first_word_frequency_list(self):
        obj = FestivalNames()
        data = obj.convert_list_to_first_word_frequency_list()

    def test_convert_list_to_first_word_frequency_list(self):
        obj = FestivalNames()

        data = obj.convert_list_to_first_word_frequency_list()
        print obj.filter_non_repeating_names(data)

if __name__ == '__main__':
    unittest.main()
