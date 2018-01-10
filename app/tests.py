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
        self.content = "Mumford & Sons Little lion Man \nMumford & Sons The Cave \nRihanna Umbrella"

    def test_initialize_word_count_has_default_content(self):
        obj = FestivalNames()
        self.assertIn('Lady Gaga', obj.text_content)

    def test_convert_list_to_first_word_frequency_list(self):
        obj = FestivalNames()
        obj.text_content = self.content

        data_all = obj.convert_text_content_to_first_word_dict()
        self.assertEqual(
            data_all,
            {'Rihanna': ['Rihanna Umbrella'], 'Mumford': ['Mumford & Sons Little lion Man ', 'Mumford & Sons The Cave ']}
        )

        data_unique = obj.filter_non_repeating_names(data_all)
        self.assertEqual(
            data_unique,
            {'Mumford': ['Mumford & Sons Little lion Man ', 'Mumford & Sons The Cave ']}
        )

        artist_list = obj.build_festival_names(data_unique)
        self.assertEqual(
            artist_list,
            ['Mumford & Sons']
        )

if __name__ == '__main__':
    unittest.main()
