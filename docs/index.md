#TextMasterPy Documentation  

**TextMasterPy** is a powerful Python framework designed for text analysis and processing, primarily targeting **English** and **Arabic** languages.  
It consists of **33 generic functions**, categorized into three main groups:  


General Processing Functions: Applicable to both English and Arabic.

English-Specific Functions: Dedicated functions for English language processing.

Arabic-Specific Functions: Functions tailored for Arabic language text processing.

This framework is designed for Python 3.12.7 and relies on Python's built-in modules string and re for enhanced text manipulation.

Key Features

Handles both English and Arabic texts with robust text processing capabilities.
Built-in text cleaning to remove extra spaces, special characters, and stop words.
Supports regex operations but keeps functions flexible for broader text analysis.
Lightweight & Efficient: Uses only built-in Python modules (string, re).
Regular Updates: The framework will be continuously improved and updated.

Function Categories

1️⃣ General Processing Functions (English & Arabic)

space_count: Counts total spaces in a text.

word_count: Counts total words.

line_count: Counts total lines.

sentence_count: Counts total sentences.

character_count: Counts characters excluding spaces.

special_characters_count: Counts punctuation marks.

specific_character_count: Counts occurrences of a specific character.

specific_word_character_count: Finds words containing a specific character.

longest_word: Identifies the longest word in text.

extra_space_clean: Removes extra spaces.

special_character_removal: Removes all punctuation marks.

word_beginning: Finds words starting with a given letter.

word_end: Finds words ending with a given letter.

repeated_words: Identifies repeated words.

word_check: Checks if a specific word exists in the text.

selected_word_length_display: Finds words of a specific length.

word_reversal: Reverses words of a specific length.

suffix_words: Identifies words ending with a specific suffix.

prefix_words: Identifies words starting with a specific prefix.

2️⃣ English-Specific Functions

vowel_consonant_count: Counts vowels & consonants.

upper_lower_count: Counts uppercase & lowercase letters.

ed_ing_count: Counts words ending in 'ed' and 'ing'.

uncontract_word: Expands English contractions (e.g., can't → cannot).

english_stop_words_removal: Removes common English stop words.

title_format: Formats titles according to capitalization rules.

definite_english_detection: Detects definite nouns (preceded by 'the').

indefinite_english_detection: Detects indefinite nouns ('a' or 'an').

sentence_capitalize: Capitalizes sentences and removes extra spaces.

3️⃣ Arabic-Specific Functions

definite_arabic: Extracts Arabic definite article words (ال).

feminine_arabic_sign: Identifies words ending in ة (Teh Marbuta).

feminine_plural_arabic: Identifies words with feminine plural suffixes.

diacritics_removal: Removes diacritics from Arabic text.

singular_extended_arabic: Identifies singular extended Arabic words (اء).

Getting Started

To get started, install TextMasterPy using:

pip install textmasterpy

Then, import it in your Python script:

import textmasterpy
print("TextMasterPy is ready to use!")

If you want to learn more about a specific function, use the built-in help() method:

help(textmasterpy.englishprocessing.uncontract_word)

More Resources

📦 PyPI: TextMasterPy on PyPI
https://pypi.org/project/textmasterpy/1.0.1/ 
For full Documentation: GitHub Repository

Best wishes, and happy coding!

