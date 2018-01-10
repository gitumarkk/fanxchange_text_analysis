import os


class Base(object):
    def __init__(self, data_file_path=None):
        """Initializes the object by getting the input data and
            creating the instance variable text_data

        Args:
            data_file_path (str): The file path to be opened.
        """
        if not data_file_path:
            data_file_path = 'data/festival.txt'

        self.text_content = self.get_data_from_file(data_file_path)


    def get_data_from_file(self, data_file_path):
        """Open's a file provided in the key word and reads the data from it

        Args:
            data_file_path (str): The file path to be opened.

        Returns:
            list: The file content in as a list

        """
        with open(data_file_path) as input_file:
            content = input_file.read()
        return content
