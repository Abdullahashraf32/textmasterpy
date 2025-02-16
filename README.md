# TextMasterPy Framework

This framework is designed to assist developers in performing efficient text analysis and processing tasks for both English and Arabic texts. It is built to handle a variety of common text processing operations and is structured into three categories: general processing functions (usable for both English and Arabic), English-specific functions, and Arabic-specific functions. 
Author: Abdullah Ashraf
name: TextMasterPy framework
version: 1.0.1
project date: 11/02/2025
date created: 09/02/2025
update date: 12/02/2025

FRAMEWORK OVERVIEW

This framework consists of **33 generic functions** organized into three main categories:

1. **General Processing Functions**: Functions applicable to both English and Arabic texts.
2. **English-Specific Functions**: Functions designed specifically for English language processing.
3. **Arabic-Specific Functions**: Functions designed specifically for Arabic language processing.

The framework is designed for Python 3.12.7 and depends on some Python built-in modules, specifically `string` and `re`.

- The **`string` module** is used for accessing predefined ASCII tables and punctuation lists, which simplifies text filtering.
- The **`re` module** is used for regular expression-based operations, though it is intentionally minimized to keep functions as generic and flexible as possible.

This framework will be updated regularly to include new features and improvements.

## Function Categories

### General Processing Functions (Applicable to Both English and Arabic)

1. **space_count**: Counts the total number of spaces in the given text.
2. **word_count**: Counts the total number of words in the given text.
3. **line_count**: Counts the total number of lines in the given text.
4. **sentence_count**: Counts the total number of sentences in the given text.
5. **character_count**: Counts the total number of characters, excluding spaces.
6. **special_characters_count**: Counts the total number of punctuation marks.
7. **specific_character_count**: Counts occurrences of a specific character in the text.
8. **specific_word_character_count**: Counts words containing a specific character.
9. **longest_word**: Finds and returns the longest word in the text.
10. **extra_space_clean**: Removes extra spaces from the text.
11. **special_character_removal**: Removes punctuation marks from the text.
12. **word_beginning**: Identifies and counts words beginning with a specified letter.
13. **word_end**: Identifies and counts words ending with a specified character.
14. **repeated_words**: Identifies and counts repeated words.
15. **word_check**: Checks if a specific word exists within the text.
16. **selected_word_length_display**: Displays words of a specified length.
17. **word_reversal**: Reverses words in the text that meet a length criterion.
18. **suffix_words**: Identifies words ending with a specified suffix.
19. **prefix_words**: Identifies words starting with a specified prefix.

### English-Specific Functions

1. **vowel_consonant_count**: Counts vowels and consonants in the text.
2. **upper_lower_count**: Counts uppercase and lowercase letters in the text.
3. **ed_ing_count**: Counts words ending with 'ed' and 'ing'.
4. **uncontract_word**: Expands contracted words to their full forms.
5. **english_stop_words_removal**: Removes common English stop words.
6. **title_format**: Formats the title according to English title capitalization rules.
7. **definite_english_detection**: Detects and counts definite nouns preceded by "the".
8. **indefinite_english_detection**: Detects and counts indefinite nouns preceded by "a" or "an".
9. **sentence_capitalize**: Capitalizes the first letter of each sentence in a string.

### Arabic-Specific Functions

1. **definite_arabic**: Identifies and extracts words beginning with the Arabic definite article "ال".
2. **feminine_arabic_sign**: Identifies words ending with the Arabic feminine sign "ة".
3. **feminine_plural_arabic**: Identifies words ending with Arabic feminine plural suffixes.
4. **diacritics_removal**: Removes diacritics from Arabic text.
5. **singular_extended_arabic**: Identifies singular extended Arabic nouns ending with "اء".

USAGE EXAMPLE

Here are some examples about how to use the framework:
Below is an example of how you can use the `space_count` function:

import textmasterpy
print(textmasterpy.generalprocessing("This is an example text."))
Another example about how to use title_format function:
import textmasterpy
print(textmasterpy.englishprocessing.title_format("the old man and the sea"))
Another third example about how to use diacritics_removal function:
import textmasterpy
print(textmasterpy.arabicprocessing.diacritics_removal("هَذَا أَخِي الصَّغِيرُ"))
HELP FUNCTION
For detailed information about any specific function, you can use Python's built-in help() function:

import textmasterpy
help(textmasterpy.generalprocessing.character_count)

INSTALLATION
To install this framework, simply clone the repository:
https://github.com/Abdullahashraf32/textmasterpy/tree/textmasterpy
Ensure you have Python 3 installed.
CONTRIBUTIONS
TextMasterPy is a collaborative effort built with passion and dedication. This project would not have been possible without the contributions, insights, and support from a dedicated team of developers, linguists, and tech enthusiasts. We believe in the power of teamwork and collective innovation, whether in refining algorithms, in enhancing functionality, or in improving documentation. Every contribution has played a vital role in shaping this framework. We warmly welcome new contributors. If you have ideas for improvement, bug fixes, or new feature suggestions, feel free to submit a pull request or open an issue on our GitHub repository. Your input is invaluable in making TextMasterPy even better. 
LICENSE
This framework is open-source and available under the MIT License.
Best wishes!