import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
__version__ = "1.0.1"
__all__ = [
    "space_count", "word_count", "line_count", "sentence_count", "character_count",
    "special_characters_count", "specific_character_count", "specific_word_character_count",
    "longest_word", "extra_space_clean", "special_character_removal", "word_beginning",
    "word_end", "repeated_words", "word_check", "selected_word_length_display",
    "word_reversal", "suffix_words", "prefix_words", "vowel_consonant_count",
    "upper_lower_count", "ed_ing_count", "uncontract_word", "english_stop_words_removal",
    "title_format", "definite_english_detection", "indefinite_english_detection",
    "sentence_capitalize", "definite_arabic", "feminine_arabic_sign",
    "feminine_plural_arabic", "diacritics_removal", "singular_extended_arabic"
]
try:
    from .generalprocessing import (
        space_count, word_count, line_count, sentence_count, character_count,
        special_characters_count, specific_character_count, specific_word_character_count,
        longest_word, extra_space_clean, special_character_removal, word_beginning,
        word_end, repeated_words, word_check, selected_word_length_display,
        word_reversal, suffix_words, prefix_words
    )
    from .englishprocessing import (
        vowel_consonant_count, upper_lower_count, ed_ing_count, uncontract_word,
        english_stop_words_removal, title_format, definite_english_detection,
        indefinite_english_detection, sentence_capitalize
    )
    from .arabicprocessing import (
        definite_arabic, feminine_arabic_sign, feminine_plural_arabic,
        diacritics_removal, singular_extended_arabic
    )
    logger.info("Text Processing Framework has been successfully imported!")
except ImportError as exception:
    logger.error("Error importing modules.")
 