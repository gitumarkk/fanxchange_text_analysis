# Motivations
The codebase contained in this repo is part of a problem set specified by FanXchange.

# Requirements
The code base was constrained to run using `python 2.7` using the standard python libraries.

## Directory structure
The directory structure of the project is as follows:

```
fanxchange_text_analysis/
├── README.md
└── app
    ├── __init__.py
    ├── base.py
    ├── data
    │   └── festival.txt
    ├── festival_names.py
    ├── tests.py
    └── word_counter.py
```

# Code Logic

## Unittest
To run the unittest, cd into the `app/` folder, and the command to run the unit test is:

```$ python tests.py```

## Task 1
For the successful completion of the task, the code implemented should get the total number of words in a test file as well as the 10 most common words and the number of occurences for this.

To this end, the code for Task 1 is in the `word_counter.py` file.  In order to fulfill the task requirements, the following code needs to be run:

```$ python word_counter.py <file_path>```

If the file path has not been specified, the `.\data\festival.txt` file will be used instead.

The `word_counter` module contains the `WordCounter` class which inherits the `Base` class. This is a shared class that contains a file reader and stores the text content in an instance variable. The reason for the `Base` class is to be in line with the **DRY** principle as both tasks requires a file to be read.

The `WordCounter` class contains two main functions:
* The first one is the `get_total_words` function which processes the file input and get's the count of words. This is a straighforward function and is self explanatory.
* The second function is `get_most_common_words` which takes in an optional `limit` variable that was added for testability. In order to find the most common words, the function uses the python inbuilt `collection.Counter` module. As it's a native, it's optimized as well as provides a convenience function to return the common words encountered.


## Task 2
For the successful completion of the task, the code implemented should find the unique festival names based on the specified parameters.

To this end, the code for Task 2 is in the `festival_names` file.  The command to run test the functionality is:

```$ python festival_names.py <file_path>```

If the file path has not been specified, the `.\data\festival.txt` file will be used instead.

The `festival_names` module contains the `FestivalNames` class which inherits the `Base` class. The purpose of the base class has been previously explained.


The `FestivalNames` contains several methods which has been explained below.

### `convert_text_content_to_first_word_dict`.

Several assumptions have been made about the festival names which includes:
* They must contain at least the first word in a sentence, which is tagged as the pseudo festival name.
* The psuedo festival name must occur as the first word in at least 2 sentences.

Based on this assumption, the method creates a  festival dictionary containing the pseudo festival name which is the first word in the sentence as a key, and the sentences as a list of values, which will be filtered out later.

### `filter_non_repeating_names`.
As a unique festival name must occur in at least 2 sentences, this method filters out pseudo festival names keys in the festival dictionary where the value containing the sentences only have one item in the list.


### `build_festival_names`
Now that the festival dictionary only has pseudo names that have multiple occurences, the actual festival names need to be determined. The unique festival name is assumed to be the first n characters between 2 strings that are equal. Thus, this method calls the `get_sentence_commonality` method and passes in only 2 strings as is this is the minimum number of strings required to find the real festival name.

### `get_sentence_commonality`
Given 2 sentences, returns the festival name which is taken to be the first set of common characters between 2 strings.
