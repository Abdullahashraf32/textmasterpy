#general functions can be used with english and arabic languages.
import string
def space_count(text):
  """It counts the total number of spaces in the given text. This function takes a single parameter: the text to analyze. It returns the total count of spaces found in the text. Spaces include both single spaces and multiple consecutive spaces."""
  total_count=0
  for i in text:
    if i==" ":
      total_count+=1
  return total_count
def word_count(text):
  """It counts the total number of words in the given text. This function takes a single parameter: the text to analyze. It returns the total count of words found in the text. Words are identified by splitting the text at whitespace characters."""
  total_words=[]
  total_words = text.split()
  return len(total_words)
def line_count(text):
  """It counts the total number of lines in the given text. This function takes a single parameter: the text to analyze. It returns the total count of lines found in the text. Lines are identified by newline characters ('\n')."""
  total_lines=1
  for i in text:
    if i=="\n":
      total_lines+=1
  return total_lines
def sentence_count(text):
  """It counts the total number of sentences in the given text. This function takes a single parameter: the text to analyze. It returns the total count of sentences found in the text. Sentences are identified by terminal punctuation marks such as periods (.), exclamation marks (!), and question marks (?). The function supports both English and Arabic punctuation marks."""
  total_sentences=0
  for i in text:
    if i in "?!.ـ؟":
      total_sentences+=1
  return total_sentences
def character_count(text):
  """It counts the total number of characters in the given text, excluding spaces. This function takes a single parameter: the text to analyze. It returns the total count of characters in the text. The function is useful for determining the length of the text in terms of characters."""
  total_characters=0
  for i in text:
    if i!=" ":
      total_characters+=1
  return total_characters
def special_characters_count(text):
  """It counts the total number of punctuation marks in the given text. This function takes a single parameter: the text to analyze. It returns the total count of punctuation marks found in the text. The function supports both English and Arabic punctuation marks and provides a list of the found punctuation marks."""
  arabic_punctuation="،؛؟:•\"“”'()[]{}<>ـ"
  total_special_characters=0
  punctuations_found=[]
  for i in text:
    if i in string.punctuation and i in arabic_punctuation:
      total_special_characters+=1
      punctuations_found.append(i)
  print(f"Punctuations found are {' '.join(punctuations_found)} and the total number of punctuations is ")
  return total_special_characters
def specific_character_count(text,character):
  """It counts the total number of occurrences of a specific character in the given text. This function takes two parameters: the text to analyze and the character to count. It returns the total count of the specified character in the entire text. The function is case-sensitive and counts the character exactly as provided."""
  specific_count=0
  arabic_punctuation="،؛؟:•\"“”'()[]{}<>ـ"
  for i in text:
    if i==character:
      specific_count+=1
  return specific_count
def specific_word_character_count(text,letter):
  """It counts the total number of words containing a specific character within the given text. This function takes two parameters: the text to analyze and the character to search for within the words. It returns the total count of unique words that contain the specified character at least once. The function is case-insensitive and ignores punctuation and digits attached to the words."""
  specific_list=[]
  specific_count=0
  splitted_text=text.split()
  for i in splitted_text:
    i=i.strip(string.punctuation+string.digits)
    if letter in i:
      specific_list.append(i)
      specific_count+=1
  print(f"The total words that contain  the character: \"{letter}\" are: {', '.join(specific_list)}.")
  return specific_count
def longest_word(user_text):
  """It finds and returns the longest word in the given text. This function takes a single parameter: the text to analyze. In case there are multiple words of the same maximum length, the first one encountered is returned. The function ignores punctuation and digits attached to the words."""
  words=""
  splitted_text=user_text.split()
  for i in splitted_text:
    i=i.strip(string.punctuation+string.digits)
    if len(i)>len(words):
      words=i
  return words
def extra_space_clean(unfiltered_text):
  """It filters the given text from extra spaces. This function takes a single parameter: the text you need to filter from extra spaces. It returns a new string filtered from all extra spaces, ensuring that each single word is separated by a single space only. The function is useful for cleaning up text that may have inconsistent spacing. It supports both Arabic and English."""
  """This function cleans the given text from extra spaces that can be found within your text"""
  splitted_text=unfiltered_text.split()
  return " ".join(splitted_text)
def special_character_removal(uncleaned_text):
  """It removes punctuation marks from the given text. This function takes a single parameter: the text from which to remove punctuation marks. It returns a new string with all punctuation marks removed. The function supports both English and Arabic punctuation marks."""
  arabic_punctuation="،؛؟:•\"“”'()[]{}<>ـ"
  clean_text=""
  for i in uncleaned_text:
    if i not in string.punctuation and i not in arabic_punctuation:
      clean_text+=i
  return clean_text
def word_beginning(extract, letter):
  """It identifies and counts words in the given text that begin with the specified letter. This function takes two parameters: the text to analyze and the letter to search for at the beginning of words. It returns the total count of words that start with the specified letter and prints a list of these words. The function is case-insensitive and ignores punctuation and digits attached to the words."""
  beginning_word_list=[]
  split_text=extract.split()
  beginning_count=0
  for i in split_text:
    i=i.strip(string.punctuation+string.digits)
    if i[0].lower()==letter.lower():
      beginning_word_list.append(i)
      beginning_count+=1
  print(f"The words that are found begin with the character \"{letter}\" are: \"{', '.join(beginning_word_list)}\", and its total count is: {beginning_count}")
  return beginning_count
def word_end(text,character):
  """It identifies and counts words in the given text that end with the specified character. This function takes two parameters: the text to analyze and the character to search for at the end of words. It returns the total count of words that end with the specified character and prints a list of these words. The function is case-insensitive and ignores punctuation and digits attached to the words."""
  splitted_text=text.split()
  end_count=0
  end_word_list=[]
  for i in splitted_text:
    i=i.strip(string.punctuation+string.digits)
    if i[-1].lower()==character.lower():
      end_word_list.append(i)
      end_count+=1
  print(f"The words that end with the letter \"{character}\" are: \"{', '.join(end_word_list)}\", and its total count is: ")
  return end_count
def repeated_words(text):
  """It identifies and counts repeated words in the given text. This function takes a single parameter: the text to analyze. It returns the total count of unique words that appear more than once in the text. The function is case-insensitive and ignores punctuation and digits attached to the words."""
  total_text=[]
  repeated_text=[]
  splitted_text=text.split()
  for i in splitted_text:
    i=i.strip(string.punctuation+string.digits).lower()
    if i in total_text:
      if i not in repeated_text:
        repeated_text.append(i)
    else:
      total_text.append(i)
  print(f"The repeated words that are found are: \"{', '.join(repeated_text)}\", and the total count of repeated words is: ")
  return len(repeated_text)
def word_check(text,word):
  """It checks if the specified word exists within the given text. This function takes two parameters: the text to search within and the word to search for. It returns True if the word is found in the text, otherwise it returns False. The function is case-insensitive and ignores punctuation and digits attached to the words."""
  arabic_punctuation="،؛؟:•\"“”'()[]{}<>ـ"
  text=text.split()
  for i in text:
    i=i.strip(string.punctuation+string.digits+arabic_punctuation)
    if i==word:
      return True
  return False
def selected_word_length_display(text,length):
  """It extracts and displays words from the given text that have a specific length. This function takes two parameters: the text to analyze and the desired length of words to extract. It returns a string containing the words that match the specified length, or None if no such words are found."""
  arabic_punctuation="،؛؟:•\"“”'()[]{}<>ـ"
  selected_text=[]
  length=int(length)
  splitted_text=text.split()
  for i in splitted_text:
    i=i.strip(string.punctuation+string.digits+arabic_punctuation)
    if len(i)==length:
      selected_text.append(i)
  if not selected_text:
    return None
  return f"The words that its total length is {length} within your text are: \"{', '.join(selected_text)}\""
def word_reversal(text,number):
  """ This function reverses words in the given text that have a length greater than or equal to the specified number. This function takes two parameters: the text to process and the minimum length of words to reverse. It returns a new string where words meeting the length criterion are reversed, while others remain unchanged."""
  splitted_text=text.split()
  result=[]
  for i in splitted_text:
    if len(i)>=number:
      result.append(i[::-1])
    else:
      result.append(i)
  return " ".join(result)
def suffix_words(text,suffix):
  """ This function analyzes the given text and identifies words that end with the specified suffix. It takes two parameters: the text to analyze and the suffix to search for. The function returns a list of words that end with the given suffix and the total count of such words. The function is case-insensitive and ignores punctuation and digits attached to the words."""
  suffix_words_list=[]
  suffix_count=0
  splitted_text=text.split()
  for i in splitted_text:
    i=i.strip(string.punctuation+string.digits)
    if len(i)>len(suffix) and i[-len(suffix):]==suffix:
      suffix_words_list.append(i)
      suffix_count+=1 
  print(f"The total words that end with \"{suffix}\" are: \"{', '.join(suffix_words_list)}\".\nThe total count of the words that end with \"{suffix}\" is: ")
  return suffix_count
def prefix_words(text,prefix):
  """This function analyzes the given text and identifies words that start with the specified prefix. It takes two parameters: the text to analyze and the prefix to search for. The function returns a list of words that start with the given prefix and the total count of such words. The function is  case-insensitive and ignores punctuation and digits attached to the words."""
  prefix_words_list=[]
  prefix_count=0
  splitted_text=text.split()
  for i in splitted_text:
    i=i.strip(string.punctuation+string.digits)
    if i[:len(prefix)]==prefix:
      prefix_words_list.append(i)
      prefix_count+=1 
  print(f"The total words that end with \"{prefix}\" are: \"{', '.join(prefix_words_list)}\".\nThe total count of the words that end with \"{prefix}\" is: ")
  return prefix_count